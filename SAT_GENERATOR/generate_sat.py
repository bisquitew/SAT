import random
from itertools import combinations

def generate_unsat_cnf(num_vars, num_clauses):
    """Generate an unsatisfiable CNF by creating contradictory constraints"""
    cnf = []
    
    # Core contradiction (x1 AND -x1)
    cnf.append([1])
    cnf.append([-1])
    
    # Add random clauses ensuring UNSAT remains
    for _ in range(num_clauses - 2):
        clause = []
        clause_size = random.randint(2, 4)
        vars_in_clause = random.sample(range(1, num_vars+1), min(clause_size, num_vars))
        for v in vars_in_clause:
            clause.append(v * random.choice([-1, 1]))
        cnf.append(clause)
    
    return cnf

def generate_sat_cnf(num_vars, num_clauses):
    """Generate a satisfiable CNF by ensuring at least one solution exists"""
    cnf = []
    solution = {v: random.choice([True, False]) for v in range(1, num_vars+1)}
    
    for _ in range(num_clauses):
        while True:
            clause_size = random.randint(2, 4)
            vars_in_clause = random.sample(range(1, num_vars+1), min(clause_size, num_vars))
            clause = []
            for v in vars_in_clause:
                if random.random() < 0.7:  # Bias toward including solution literals
                    clause.append(v if solution[v] else -v)
                else:
                    clause.append(v * random.choice([-1, 1]))
            
            # Ensure clause isn't tautological
            if not any(lit in clause and -lit in clause for lit in clause):
                break
        cnf.append(clause)
    
    return cnf

def write_dimacs(cnf, num_vars, filename):
    with open(filename, 'w') as f:
        f.write(f"p cnf {num_vars} {len(cnf)}\n")
        for clause in cnf:
            f.write(" ".join(map(str, clause)) + " 0\n")

# Generate benchmark files
sizes = [
    (100, 2400),   # Small
    (3000, 6000),  # Medium
    (5000, 7500)  # Large
]

for i, (vars, clauses) in enumerate(sizes):
    # Generate UNSAT
    unsat_cnf = generate_unsat_cnf(vars, clauses)
    write_dimacs(unsat_cnf, vars, f"unsat_{vars}v_{clauses}c.cnf")
    
    # Generate SAT
    sat_cnf = generate_sat_cnf(vars, clauses)
    write_dimacs(sat_cnf, vars, f"sat_{vars}v_{clauses}c.cnf")

print("Generated benchmark files:")
print("\n".join([f"sat_{v}v_{c}c.cnf" for v,c in sizes] + [f"unsat_{v}v_{c}c.cnf" for v,c in sizes]))