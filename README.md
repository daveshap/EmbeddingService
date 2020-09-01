# Google Universal Sentence Encoder Microservice

Ultra simple REST API microservice for handling Google Universal Sentence Encoder.

## Tutorial

1. Create an Anaconda environment with `tensorflow_hub` and `flask`.
2. Start the Anaconda environment and run `USEv4_microservice.py`.
3. Use the `client.py` to get an example of the usage.
4. Simply perform an HTTP POST to http://localhost:999 where the payload is a list of strings i.e. `["This is a string to embed.", "This is also a string to embed."]`
5. The microservice will embed the sentences as semantic vectors and return a list of dictionaries i.e. `[{"string":"original sentence","vector":"#####"}]`

## Examples

How the microservice looks:

```bash
(tf2_gpu) C:\USE_microservice>python USEv4_microservice.py
2020-09-01 16:04:28.485293: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudart64_101.dll
2020-09-01 16:04:31.989725: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library nvcuda.dll
2020-09-01 16:04:32.093989: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1555] Found device 0 with properties:
pciBusID: 0000:01:00.0 name: GeForce RTX 2070 computeCapability: 7.5
coreClock: 1.71GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 417.29GiB/s
2020-09-01 16:04:32.105438: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudart64_101.dll
2020-09-01 16:04:32.116839: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cublas64_10.dll
2020-09-01 16:04:32.136340: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cufft64_10.dll
2020-09-01 16:04:32.143902: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library curand64_10.dll
2020-09-01 16:04:32.151881: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cusolver64_10.dll
2020-09-01 16:04:32.168041: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cusparse64_10.dll
2020-09-01 16:04:32.184134: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudnn64_7.dll
2020-09-01 16:04:32.189162: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-09-01 16:04:32.193567: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
2020-09-01 16:04:32.210366: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1555] Found device 0 with properties:
pciBusID: 0000:01:00.0 name: GeForce RTX 2070 computeCapability: 7.5
coreClock: 1.71GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 417.29GiB/s
2020-09-01 16:04:32.217849: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudart64_101.dll
2020-09-01 16:04:32.222040: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cublas64_10.dll
2020-09-01 16:04:32.226238: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cufft64_10.dll
2020-09-01 16:04:32.229364: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library curand64_10.dll
2020-09-01 16:04:32.233889: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cusolver64_10.dll
2020-09-01 16:04:32.238114: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cusparse64_10.dll
2020-09-01 16:04:32.242769: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudnn64_7.dll
2020-09-01 16:04:32.246926: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-09-01 16:04:32.938683: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1096] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-09-01 16:04:32.942336: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102]      0
2020-09-01 16:04:32.944987: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] 0:   N
2020-09-01 16:04:32.950180: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1241] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6306 MB memory) -> physical GPU (device: 0, name: GeForce RTX 2070, pci bus id: 0000:01:00.0, compute capability: 7.5)
 * Serving Flask app "encoder" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
INFO:werkzeug: * Running on http://0.0.0.0:999/ (Press CTRL+C to quit)
['This is a sentence', 'this is a second sentence']
2020-09-01 16:04:47.884356: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cublas64_10.dll
INFO:werkzeug:127.0.0.1 - - [01/Sep/2020 16:04:48] "[37mPOST / HTTP/1.1[0m" 200 -
['This is a sentence', 'this is a second sentence']
INFO:werkzeug:127.0.0.1 - - [01/Sep/2020 16:04:52] "[37mPOST / HTTP/1.1[0m" 200 -
['This is a sentence', 'this is a second sentence']
INFO:werkzeug:127.0.0.1 - - [01/Sep/2020 16:04:56] "[37mPOST / HTTP/1.1[0m" 200 -
```

How the client looks:

```bash
C:\USE_microservice>python client.py
[{'string': 'This is a sentence',
  'vector': '[0.028817661106586456, -0.020200150087475777, '
            '0.010696266777813435, 0.03850530833005905, -0.09253700077533722, '
            '0.017527734860777855, -0.04711754620075226, 0.047852084040641785, '
			........
            '0.1103242039680481, -0.013840682804584503, -0.009360543452203274, '
            '0.02323107048869133, 0.0042100404389202595, '
            '-0.028969207778573036, 0.008764670230448246, '
            '0.08242126554250717]'},
 {'string': 'this is a second sentence',
  'vector': '[0.04119128733873367, -0.033451974391937256, '
            '-0.02913030795753002, 0.07749398797750473, -0.09640706330537796, '
            '0.033736273646354675, -0.01458499301224947, 0.012801065109670162, '
			........
            '0.01435331255197525, -0.045849379152059555, '
            '-0.017022253945469856, -0.02670147269964218, '
            '-0.04068242385983467, 0.08653835952281952]'}]
Total time: 0.017948627471923828

C:\USE_microservice>
```