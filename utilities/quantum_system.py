import itertools
import numpy as np
import itertools
#import utilities.braket_formalism as bf
import utilities.maths as  maths
import copy
import math
import utilities.matrix_formalism as mf
import utilities.braket_formalism as  bf
import operator
from typing import List

from collections import namedtuple

leaf_sys_signature = namedtuple('leaf_sys_signature','name dim qm_nums_names' )



tmp_lst = []

class node:
    def __init__(self, id,children:list  = None):
        self.id = id
        if children is None:
            self.children = []
        else:
            self.children = children
    def has_child(self):
        if len(self.children)>0:
            return True
        else:
            return False

    def add_child(self, child):
        self.children.append(child)

    def get_depth(self, target_node):
        depth = 0

    def find_leaves_avoid(self, id):
        res = []
        self.find_leaves_avoid_imp(id, res)

        avoid_index = 0

        for i in range(len(res)):
            if res[i].id==id:
                avoid_index = i
                break

        left_side_leaves = res[0:avoid_index]
        right_side_leaves = res[avoid_index+1:]

        #res.index(id)

        return left_side_leaves, res[avoid_index],right_side_leaves




    def find_leaves_avoid_imp(self, id ,res):
        
        if self.id==id:
            #res.append('avoid_ found'+  ' ' + id)
            res.append(self)
                
        elif self.has_child():
            for child in self.children:
                child.find_leaves_avoid_imp(id, res)
        else:
            res.append(self)



    def find_leaves(self):
        res = []
        self.find_leaves_imp(res)
        return res    
    
    def find_leaves_imp(self,res:list):
        if self.has_child():
            for child in self.children:
                child.find_leaves_imp(res)
        else:
            res.append(self)

    def find_node(self, id):
        res = []
        depths = []

        self.find_node_imp(id, res, depths, new_depth_0=0)
        return res#, depths




    def find_node_imp(self,data, res:list, depths:list, new_depth_0:int ):

        new_depth = copy.deepcopy(new_depth_0)
        
        if self.id==data:
            res.append(self)
            #new_depth+=1
            depths.append(new_depth)
            
        if self.has_child():
            new_depth +=1
            for child in self.children:
                
                child.find_node_imp( data, res, depths, new_depth)

    
    def get_nodes(self, depth):
        
        res = []

        self.get_nodes_imp(depth, 0, res)
        return res

    
    def get_nodes_imp(self, depth, curr_depth, res:list):
        if depth == curr_depth:
            res.append(self)
        else:
            if self.has_child():
                curr_depth+=1
                for child in self.children:
                    child.get_nodes_imp(depth, copy.deepcopy(curr_depth), res)



    def __repr__(self):
        return self.id

class tree:
    def __init__(self, root_node:node):
        self.root_node  = root_node

    def insert_node(self, parent_node_id, new_child):
        parent_node = self.root_node.find_node(parent_node_id)[0]
        parent_node.add_child(new_child)
        #parent_node.children.append(new_child)
        print('inserted')



class quantum_system_node(node):
    def __init__(self, id, base_states:mf.hilber_space_bases = None,operators = {},children:list  = None, dim = 1):
        node.__init__(self, id, children )
        self.operators = operators
        self.base_states:mf.hilber_space_bases = base_states
        if self.base_states!=None:
            self.dim = self.base_states.dim
        else:
            self.dim = dim
        if len(self.children)>=1:
            self.create_hilbert_space()


    


    def create_hilbert_space(self):
        simple_systems = self.find_leaves()

        """
        children_system_bases = []
        
        
        for sys in simple_systems:
            if sys.base_states!=None:
                children_system_bases.append(sys.base_states)

        children_system_bases = list(map( lambda x:x.base_states , simple_systems))
        """
        children_system_bases = [ x.base_states for x in simple_systems if x.base_states!=None ]

        self.base_states = mf.hilber_space_bases.kron_hilber_spaces(children_system_bases)

    #def find_operator(operator_id) -> node:

    def find_operator(self, operator_id):
        res = []
        depths = []

        self.find_operator_imp(operator_id, res, depths, new_depth_0=0)
        return res[0].id

    def find_operator_imp(self,operator_id, res:list, depths:list, new_depth_0:int ):

        new_depth = copy.deepcopy(new_depth_0)
        
        if operator_id in self.operators:
            res.append(self)
            #new_depth+=1
            depths.append(new_depth)
            
        if self.has_child():
            new_depth +=1
            for child in self.children:
                
                child.find_operator_imp( operator_id, res, depths, new_depth)



    def create_operator(self, operator_id = '', operator_system_id = ''):

        if operator_system_id == '':
            operator_system_id = self.find_operator(operator_id)

        left_systems = []

        left_systems, system, right_systems = self.find_leaves_avoid(operator_system_id) 
        print(left_systems)
        print(system)
        print(right_systems)

        op = system.operators[operator_id]

        ops_to_kron = []

        left_dims =  list(map(lambda x: x.dim, left_systems))

        left_dim = list(itertools.accumulate(left_dims,operator.mul ))[-1] if left_dims!=[] else 1

        right_dims =  list(map(lambda x: x.dim, right_systems)) 

        right_dim = list(itertools.accumulate(right_dims,operator.mul ))[-1] if right_dims!=[] else 1




        #right_dim = 1
        


        #left_dim = 1 * list( itertools.accumulate(left_systems , lambda x,y: x.dim*y.dim) )[-1]
        #right_dim = 1*  list( itertools.accumulate(right_systems , lambda x,y: x.dim*y.dim) )[-1] != None
        """
        for left_sys in left_systems:
            left_dim*=left_sys.dim

        for right_sys in right_systems:
            right_dim*=right_sys.dim
        """

        I_left = mf.MatrixOperator.create_id_matrix_op(dim = left_dim)
        I_right = mf.MatrixOperator.create_id_matrix_op(dim = right_dim)

        return I_left**op**I_right

        #children_sys_node = list(filter( lambda x: x.id == system_id,self.children))
    

class quantum_system_tree(tree):

    def create_basis_trf_matrix(self, basis_name:str):
        leaf_systems:list[quantum_system_node] = self.root_node.find_leaves()

        basis_trf_matrixes = [ leaf_system.base_states.create_trf_op(basis_name) for leaf_system in leaf_systems]
        print('basis_trf')

        return list(itertools.accumulate( basis_trf_matrixes,lambda x, y: x**y ))[-1]



    def __init__(self, root_quantum_system_node:quantum_system_node ):
        self.root_node = root_quantum_system_node
    
    def insert_node(self, parent_node_id, new_child):
        super().insert_node(parent_node_id, new_child)
        
        self.root_node.create_hilbert_space()
        parent_node = self.find_subsystem(parent_node_id)[-1]
        parent_node.create_hilbert_space()

    def create_operator(self, operator_id , subsys_id='', operator_sys = '' )->mf.MatrixOperator:



        if subsys_id == '':
            return self.root_node.create_operator(operator_id= operator_id, operator_system_id=operator_sys)


        else:
            subsys_node = self.root_node.find_node(subsys_id)[0]

            return subsys_node.create_operator(operator_id= operator_id, operator_system_id=operator_sys)
    
    

    def find_subsystem(self, subsystem_id)->quantum_system_node:
        return self.root_node.find_node(subsystem_id)