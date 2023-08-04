# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team
import grpc
from .server import MIIServer
from .client import MIIClient, mii_query_handle
from .deployment import deploy
from .terminate import terminate
from .config import DeploymentType, Tasks
from .aml_related.utils import aml_output_path

from .config import MIIConfig, DeploymentConfig
from .grpc_related.proto import modelresponse_pb2_grpc

__version__ = "0.0.0"
non_persistent_models = {}
try:
    from .version import __version__
except ImportError:
    pass
