#!/usr/bin/env python3
# Template auto-generated by polygraphy [v0.36.2] on 06/15/22 at 04:23:28
# Generation Command: /usr/local/bin/polygraphy run model.onnx --onnxrt --trt --workspace 1000000000 --save-engine=model-FP32.plan --atol 1e-3 --rtol 1e-3 --verbose --gen-script=./polygraphyRun.py --trt-min-shapes tensor-0:[1,1,28,28] --trt-opt-shapes tensor-0:[4,1,28,28] --trt-max-shapes tensor-0:[16,1,28,28] --input-shapes tensor-0:[4,1,28,28]
# This script compares /work/gitlab/tensorrt-cookbook-in-chinese/08-Tool/Polygraphy/runExample/model.onnx between ONNX Runtime and TensorRT.

from polygraphy.logger import G_LOGGER
G_LOGGER.severity = G_LOGGER.VERBOSE

from polygraphy.backend.onnxrt import OnnxrtRunner, SessionFromOnnx
from polygraphy.backend.trt import CreateConfig as CreateTrtConfig, EngineFromNetwork, NetworkFromOnnxPath, Profile, SaveEngine, TrtRunner
from polygraphy.common import TensorMetadata
from polygraphy.comparator import Comparator, CompareFunc, DataLoader
import sys

# Data Loader
data_loader = DataLoader(input_metadata=TensorMetadata().add('tensor-0', None, (4, 1, 28, 28)))

# Loaders
build_onnxrt_session = SessionFromOnnx('/work/gitlab/tensorrt-cookbook-in-chinese/08-Tool/Polygraphy/runExample/model.onnx')
parse_network_from_onnx = NetworkFromOnnxPath('/work/gitlab/tensorrt-cookbook-in-chinese/08-Tool/Polygraphy/runExample/model.onnx')
profiles = [
    Profile().add('tensor-0', min=[1, 1, 28, 28], opt=[4, 1, 28, 28], max=[16, 1, 28, 28])
]
create_trt_config = CreateTrtConfig(max_workspace_size=1000000000, profiles=profiles)
build_engine = EngineFromNetwork(parse_network_from_onnx, config=create_trt_config)
save_engine = SaveEngine(build_engine, path='model-FP32.plan')

# Runners
runners = [
    OnnxrtRunner(build_onnxrt_session),
    TrtRunner(save_engine),
]

# Runner Execution
results = Comparator.run(runners, data_loader=data_loader)

success = True
# Accuracy Comparison
compare_func = CompareFunc.simple(rtol={'': 0.001}, atol={'': 0.001})
success &= bool(Comparator.compare_accuracy(results, compare_func=compare_func))

# Report Results
cmd_run = ' '.join(sys.argv)
if not success:
    G_LOGGER.critical("FAILED | Command: {}".format(cmd_run))
G_LOGGER.finish("PASSED | Command: {}".format(cmd_run))

