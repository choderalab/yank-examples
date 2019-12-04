# Temporarily change directory to $HOME to install software
pushd .
cd $HOME

# Install Miniconda
MINICONDA=Miniconda3-latest-Linux-x86_64.sh
MINICONDA_HOME=$HOME/miniconda
MINICONDA_MD5=$(curl -s https://repo.continuum.io/miniconda/ | grep -A3 $MINICONDA | sed -n '4p' | sed -n 's/ *<td>\(.*\)<\/td> */\1/p')
wget -q http://repo.continuum.io/miniconda/$MINICONDA
if [[ $MINICONDA_MD5 != $(md5sum $MINICONDA | cut -d ' ' -f 1) ]]; then
    echo "Miniconda MD5 mismatch"
    exit 1
fi
bash $MINICONDA -bup $MINICONDA_HOME

# Configure miniconda
export PIP_ARGS="-U"
source $MINICONDA_HOME/etc/profile.d/conda.sh
# Reset default settings
rm ~/.condarc || true
# Update base environment
conda activate
conda config --add channels omnia/label/dev
conda config --add channels omnia
conda config --add channels conda-forge
conda config --set always_yes yes
conda update -yq conda pip
conda install --yes conda-build jinja2 anaconda-client

# Restore original directory
popd
