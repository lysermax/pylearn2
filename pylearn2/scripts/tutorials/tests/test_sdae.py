"""
This module tests stacked_autoencoders.ipynb
"""

import os
from nose.plugins.skip import SkipTest

from pylearn2.datasets.exc import NoDataPathError
from pylearn2.testing import no_debug_mode
from pylearn2.config import yaml_parse


@no_debug_mode
def train_yaml(yaml_file):

    train = yaml_parse.load(yaml_file)
    train.main_loop()

def train_layer1(yaml_file_path, save_path):

    yaml = open("{0}/dae_l1.yaml".format(yaml_file_path), 'r').read()
    hyper_params = {'train_stop' : 50,
                    'batch_size' : 50,
                    'monitoring_batches' : 1,
                    'nhid' : 10,
                    'max_epochs' : 1,
                    'save_path' : save_path}
    yaml = yaml % (hyper_params)
    train_yaml(yaml)

def train_layer2(yaml_file_path, save_path):

    yaml = open("{0}/dae_l2.yaml".format(yaml_file_path), 'r').read()
    hyper_params = {'train_stop' : 50,
                    'batch_size' : 50,
                    'monitoring_batches' : 1,
                    'nvis' : 10,
                    'nhid' : 10,
                    'max_epochs' : 1,
                    'save_path' : save_path}
    yaml = yaml % (hyper_params)
    train_yaml(yaml)

def train_mlp(yaml_file_path, save_path):

    yaml = open("{0}/dae_mlp.yaml".format(yaml_file_path), 'r').read()
    hyper_params = {'train_stop' : 50,
                    'valid_stop' : 50050,
                    'batch_size' : 50,
                    'max_epochs' : 1,
                    'save_path' : save_path}
    yaml = yaml % (hyper_params)
    train_yaml(yaml)

def test_sda():

    yaml_file_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),
                                                                        '..'))
    save_path = os.path.dirname(os.path.realpath(__file__))

    try:
        train_layer1(yaml_file_path, save_path)
        train_layer2(yaml_file_path, save_path)
        train_mlp(yaml_file_path, save_path)
    except NoDataPathError:
        raise SkipTest("PYLEARN2_DATA_PATH environment variable not defined")

    try:
        os.remove("{}/dae_l1.pkl".format(save_path))
        os.remove("{}/dae_l2.pkl".format(save_path))
    except:
        pass

if __name__ == '__main__':
    test_sda()
