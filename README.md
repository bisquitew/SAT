. Overview
This repository provides tools for working with the Boolean Satisfiability Problem (SAT), including:

SAT solver implementations (e.g., DPLL, DP).

Random SAT problem generators.

Utilities for parsing and manipulating CNF (Conjunctive Normal Form) formulas.

Benchmarking and testing scripts.

. Features
SAT Solvers:

DPLL algorithm

CDCL algorithm (if implemented)

Problem Generation:

Random k-SAT instances

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
. Repository Structure
SAT/  
├── CNF FILES/                
│   └── cnf_parser.py   
│   DP/
│   ├── results_davis_putnam.txt
│   ├── sat_DP_solver.cpp 
│   ├── sat_DP_solver.exe
│   DPLL/
│   ├── results_DPLL.txt
│   ├── sat_DPLL_solver.cpp
│   ├── sat_DPLL_solver.exe
│   RESOLUTION/
│   ├── results_resolution.txt
│   ├── sat_resolution_solver.cpp
│   ├── sat_resolution_solver.exe
│   SAT_GENERATOR
│   ├── generate_sat.py
│   LICENSE
│   README.md
