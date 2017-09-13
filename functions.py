__DOCKER_IMAGE__ = 'docker.io/autodesk/moldesign:moldesign_complete-0.8.0rc4'

import json
import moldesign as mdt


def run_pyscf(mol, theory, basis, functional):
    mol.set_energy_model(mdt.models.PySCFPotential,
                         theory=theory, basis=basis, functional=functional)
    mol.calculate()
    props = json.dumps(mol.properties)
    return props