from constraint import BaseConstraint
import copy
from variable import Variable
class Problem:
	def __init__(self):
		self.constraints = []
		self.variables = {}
	
	def add_constraint(self, constraint: BaseConstraint, variables: list) -> None:
		self.constraints.append((constraint, variables))

	def add_variable(self, name: str, domain: list) -> None:
		if name in self.variables:
			print("Problem: Tried to add the same variable twice")
		self.variables[name] = Variable(name, domain)


	def get_solution(self) -> map:
		self.backtracking([copy.deepcopy(x) for x in self.variables])
		# TODO: This assumes that it is always solved
		return self.variables

	def backtracking(self, unassigned: list) -> None:
		if len(unassigned) == 0:
			return
		
		variable = self.variables[unassigned[0]]
		for potential_value in variable.domain:
			if self.is_solved():
				return

			variable.value = potential_value
			if self.is_satisfying_constraints():
				self.backtracking(unassigned[1:])
			else:
				variable.value = None

	def is_solved(self):
		for name in self.variables:
			if self.variables[name].value == None:
				return False
		return self.is_satisfying_constraints()

	def is_satisfying_constraints(self):
		for constraint, variables in self.constraints:
			if not constraint.is_satisfied([self.variables[name] for name in variables]):
				return False
		return True