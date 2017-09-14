This is a proof-of-principle "component" that can be used within a workflow without
additional scripting.

This component wraps the PySCF QM code and exposes basic single point calculations with a choice of basis set, theory, and DFT functional (if using DFT).

To run it, you will need `molflow`, which doesn't work well right now.
To install:
`pip install git+https://github.com/molecular-workflow-repository/molflow`

To run this component (requires docker installed on your computer):

```bash
git clone https://github.com/molecular-workflow-repository/pyscf-component
molflow run pyscf-component benzene 6-31g rks b3lyp
```
