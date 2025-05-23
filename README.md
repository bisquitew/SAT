. Overview
This repository provides tools for working with the Boolean Satisfiability Problem (SAT), including:

SAT solver implementations (e.g., DPLL, DP).

Random SAT problem generators.

Utilities for parsing and manipulating CNF (Conjunctive Normal Form) formulas.

Benchmarking and testing scripts.

. Features
SAT Solvers:
DPLL algorithm
DP algorithm
Resolution Method
Customizable clause/variable counts

CNF Tools:
DIMACS CNF parser
Formula simplification
Benchmarking:
Performance comparisons
Statistical analysis

. Installation
Clone the repository:

git clone https://github.com/bisquitew/SAT.git
cd SAT
Install dependencies (if any):

pip install -r requirements.txt
. Usage
Running a SAT Solver using Python
python src/solver.py --input example.cnf
Generating a Random SAT Problem using Python
python src/generator.py --vars 50 --clauses 200 --ksat 3
Parsing a CNF File
using Python
from src.cnf_parser import parse_cnf  
cnf_formula = parse_cnf("example.cnf")  
