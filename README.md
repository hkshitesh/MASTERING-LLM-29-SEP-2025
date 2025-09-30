## Install Miniconda and Jupyter-Lab

conda install -c conda-forge jupyterlab

## AWS EKS CLuster Connect Commands

aws eks --region us-west-1 describe-cluster --name hiteshCluster --query cluster.status

aws eks --region us-west-1 update-kubeconfig --name hiteshCluster

