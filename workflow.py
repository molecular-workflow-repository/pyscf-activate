import molflow.definitions as mf


component = mf.WorkflowDefinition("pyscf-component")

# Functions
run_pyscf = mf.Function(sourcefile='./functions.py',
                        funcname='run_pyscf')


# Inputs
mol = component.add_input('mol',
                           'Input molecular geometry',
                           type='mdt')

basis = component.add_input('basis',
                          'Basis set identifier',
                          default='6-31g**',
                          type='str')

theory = component.add_input('theory',
                               'Level of theory',
                               default='rks',
                               type='str')

functional = component.add_input('functional',
                          'DFT functional',
                          default='b3lyp',
                          type='str')


# DAG
properties = run_pyscf(mol, theory, basis, functional)


# Outputs
component.set_output(properties, 'properties.json', type='File')

__workflow__ = component
