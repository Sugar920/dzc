临时内容2
test/srt/models/test/srt/models/test_vlm_models_qwen2_5_vl_3b_instruct.py
test_vlm_models_phi4_multimodal_instruct.py
Phi-4-multimodal-instruct   Janus-Pro-7B   test_vlm_models_janus-pro-7b.py
if is_npu():
    MODELS = [
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/mistralai/Mistral-Small-3.1-24B-Instruct-2503",
            mmmu_accuracy=0.4,
        ),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/microsoft/Phi-4-multimodal-instruct",
            mmmu_accuracy=0.4,
        ),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/Qwen/Qwen2.5-VL-3B-Instruct",
            mmmu_accuracy=0.4,
        ),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/LLM-Research/Llama-3.2-11B-Vision-Instruct", mmmu_accuracy=0.4),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/deepseek-ai/Janus-Pro-7B",
            mmmu_accuracy=0.4,
        ),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/deepseek-ai/Janus-Pro-1B",
            mmmu_accuracy=0.4,
        ),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/XiaomiMiMo/MiMo-VL-7B-RL",
            mmmu_accuracy=0.4,
        ),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/deepseek-ai/deepseek-vl2", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/openbmb/MiniCPM-V-2_6", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/openbmb/MiniCPM-o-2_6", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/google/gemma-3-4b-it", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/ZhipuAI/GLM-4.5V", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/ZhipuAI/GLM-4.1V-9B-Thinking", mmmu_accuracy=0.4),
    ]


MODELS = [
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/mistralai/Mistral-Small-3.1-24B-Instruct-2503",
            mmmu_accuracy=0.4,
        ),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/microsoft/Phi-4-multimodal-instruct",
            mmmu_accuracy=0.4,
        ),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/Qwen/Qwen2.5-VL-3B-Instruct",
            mmmu_accuracy=0.4,
        ),
        # SimpleNamespace(
        #     model="/root/.cache/modelscope/hub/models/LLM-Research/Llama-3.2-11B-Vision-Instruct",
        #     mmmu_accuracy=0.4
        # ),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/deepseek-ai/Janus-Pro-7B",
            mmmu_accuracy=0.2,
        ),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/deepseek-ai/Janus-Pro-1B",
            mmmu_accuracy=0.4,
        ),
        SimpleNamespace(
            model="/root/.cache/modelscope/hub/models/XiaomiMiMo/MiMo-VL-7B-RL",
            mmmu_accuracy=0.4,
        ),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/deepseek-ai/deepseek-vl2", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/openbmb/MiniCPM-V-2_6", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/openbmb/MiniCPM-o-2_6", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/google/gemma-3-4b-it", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/ZhipuAI/GLM-4.5V", mmmu_accuracy=0.4),
        # SimpleNamespace(model="/root/.cache/modelscope/hub/models/ZhipuAI/GLM-4.1V-9B-Thinking", mmmu_accuracy=0.4),
    ]




pip install sentence_transformers
          # apt-get update
          # apt-get install -y build-essential python3-dev python3-setuptools make cmake
          # apt-get install -y ffmpeg libavcodec-dev libavfilter-dev libavformat-dev libavutil-dev
          # git clone --recursive https://github.com/dmlc/decord
          # cd decord
          # mkdir build && cd build
          # cmake .. -DUSE_CUDA=OFF -DCMAKE_BUILD_TYPE=Release
          # make
          # cd ../python
          # python3 setup.py install
          # cd ../../
          pip install protobuf==3.20 zss pre-commit wandb>=0.16.0 tenacity==8.3.0 loguru openpyxl latex2sympy2 zstandard transformers-stream-generator tqdm-multiprocess pycocoevalcap
          pip install yt-dlp sentencepiece==0.1.99 nltk av ftfy sqlitedict==2.1.0 sacrebleu>=1.5.0 pytablewriter peft==0.2.0 black==24.1.0 isort==5.13.2 peft>=0.2.0 accelerate>=0.29.1
          pip install jsonlines httpx==0.23.3 evaluate>=0.4.0 datasets==2.16.1 numexpr xgrammar==0.1.18 numpy==1.26.4
          git clone --branch v0.3.3 --depth 1 https://github.com/EvolvingLMMs-Lab/lmms-eval.git
          cd ./lmms-eval
          nohup pip install . > lmmslog.txt 2>&1 &
          sleep 120
          export PYTHONPATH=$PYTHONPATH:$(pwd)
          cd ../
          pip install modelscope
          export MODELSCOPE_ENDPOINT=https://www.modelscope.cn
          modelscope download lmms-lab/MMMU --repo-type dataset
          cd test/srt
          python3 run_suite.py --suite per-commit-1-ascend-npu-debug




sudo add-apt-repository ppa:jonathonf/ffmpeg-4
          sudo apt-get update
          sudo apt-get install -y build-essential python3-dev python3-setuptools make cmake
          sudo apt-get install -y ffmpeg libavcodec-dev libavfilter-dev libavformat-dev libavutil-dev
          git clone --recursive https://github.com/dmlc/decord
          cd decord
          mkdir build && cd build
          cmake .. -DUSE_CUDA=OFF -DCMAKE_BUILD_TYPE=Release
          make
          cd ../python
          python3 setup.py install
          cd ../../
          git clone --branch v0.3.3 --depth 1 https://github.com/EvolvingLMMs-Lab/lmms-eval.git
          cd ./lmms-eval
          python3 setup.py install
          cd ../

          export HF_ENDPOINT=https://hf-mirror.com
          hf download lmms-lab/MMMU --repo-type dataset

# apt-get update
          # apt-get install -y build-essential python3-dev python3-setuptools make cmake
          # apt-get install -y ffmpeg libavcodec-dev libavfilter-dev libavformat-dev libavutil-dev
          # git clone --recursive https://github.com/dmlc/decord
          # cd decord
          # mkdir build && cd build
          # cmake .. -DUSE_CUDA=OFF -DCMAKE_BUILD_TYPE=Release
          # make
          # cd ../python
          # pip install .
          # cd ../../

add-apt-repository ppa:jonathonf/ffmpeg-4
          apt-get update
          apt-get install -y build-essential python3-dev python3-setuptools make cmake
          apt-get install -y ffmpeg libavcodec-dev libavfilter-dev libavformat-dev libavutil-dev
          git clone --recursive https://github.com/dmlc/decord
          cd decord
          mkdir build && cd build
          cmake .. -DUSE_CUDA=OFF -DCMAKE_BUILD_TYPE=Release
          make
          cd ../python
          python3 setup.py install
          cd ../../
          git clone --branch v0.3.3 --depth 1 https://github.com/EvolvingLMMs-Lab/lmms-eval.git
          cd ./lmms-eval
          python3 setup.py install
          cd ../


pip install protobuf==3.20 zss pre-commit wandb>=0.16.0 tenacity==8.3.0 loguru openpyxl latex2sympy2 zstandard transformers-stream-generator tqdm-multiprocess pycocoevalcap yt-dlp sentencepiece==0.1.99 nltk av ftfy sqlitedict==2.1.0 sacrebleu>=1.5.0 pytablewriter peft==0.2.0 black==24.1.0 isort==5.13.2 peft>=0.2.0 accelerate>=0.29.1 jsonlines httpx==0.23.3 evaluate>=0.4.0 datasets==2.16.1 numexpr
Searching for protobuf==3.20
Reading https://pypi.org/simple/protobuf/
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning:  is an invalid version and will not be supported in a future release
  warnings.warn(
Downloading https://files.pythonhosted.org/packages/ae/80/9eaa62a2afcc5407a6b7d2652c208f073df3a5c83b5bff90bf99553fbcf2/protobuf-3.20.0-py2.py3-none-any.whl#sha256=4eda68bd9e2a4879385e6b1ea528c976f59cd9728382005cc54c28bcce8db983
Best match: protobuf 3.20.0
Processing protobuf-3.20.0-py2.py3-none-any.whl
Installing protobuf-3.20.0-py2.py3-none-any.whl to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding protobuf 3.20.0 to easy-install.pth file
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/protobuf-3.20.0-py3.11.egg
Searching for zss
Reading https://pypi.org/simple/zss/
Downloading https://files.pythonhosted.org/packages/1e/d1/ed34d12f55d07cc1efb61d74fb2f64f46a705557f5bdd1ef1b810f0e2ec5/zss-1.2.0.tar.gz#sha256=07bb937441929ccb82961f4f7b80fbce9e2b20d0e46ddcbcbc1fcb094f585b50
Best match: zss 1.2.0
Processing zss-1.2.0.tar.gz
Writing /tmp/easy_install-g9rb_69l/zss-1.2.0/setup.cfg
Running zss-1.2.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-g9rb_69l/zss-1.2.0/egg-dist-tmp-av1r70vw
/usr/local/python3.11.13/lib/python3.11/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
zip_safe flag not set; analyzing archive contents...
Moving zss-1.2.0-py3.11.egg to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding zss 1.2.0 to easy-install.pth file
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/zss-1.2.0-py3.11.egg
Searching for pre-commit
Reading https://pypi.org/simple/pre-commit/
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning:  is an invalid version and will not be supported in a future release
  warnings.warn(
Downloading https://files.pythonhosted.org/packages/5b/a5/987a405322d78a73b66e39e4a90e4ef156fd7141bf71df987e50717c321b/pre_commit-4.3.0-py2.py3-none-any.whl#sha256=2b0747ad7e6e967169136edffee14c16e148a778a54e4f967921aa1ebf2308d8
Best match: pre-commit 4.3.0
Processing pre_commit-4.3.0-py2.py3-none-any.whl
Installing pre_commit-4.3.0-py2.py3-none-any.whl to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding pre-commit 4.3.0 to easy-install.pth file
Installing pre-commit script to /usr/local/python3.11.13/bin
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/pre_commit-4.3.0-py3.11.egg
Searching for tenacity==8.3.0
Reading https://pypi.org/simple/tenacity/
Downloading https://files.pythonhosted.org/packages/61/a1/6bb0cbebefb23641f068bb58a2bc56da9beb2b1c550242e3c540b37698f3/tenacity-8.3.0-py3-none-any.whl#sha256=3649f6443dbc0d9b01b9d8020a9c4ec7a1ff5f6f3c6c8a036ef371f573fe9185
Best match: tenacity 8.3.0
Processing tenacity-8.3.0-py3-none-any.whl
Installing tenacity-8.3.0-py3-none-any.whl to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding tenacity 8.3.0 to easy-install.pth file
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/tenacity-8.3.0-py3.11.egg
Searching for loguru
Reading https://pypi.org/simple/loguru/
Downloading https://files.pythonhosted.org/packages/0c/29/0348de65b8cc732daa3e33e67806420b2ae89bdce2b04af740289c5c6c8c/loguru-0.7.3-py3-none-any.whl#sha256=31a33c10c8e1e10422bfd431aeb5d351c7cf7fa671e3c4df004162264b28220c
Best match: loguru 0.7.3
Processing loguru-0.7.3-py3-none-any.whl
Installing loguru-0.7.3-py3-none-any.whl to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding loguru 0.7.3 to easy-install.pth file
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/loguru-0.7.3-py3.11.egg
Searching for openpyxl
Reading https://pypi.org/simple/openpyxl/
Downloading https://files.pythonhosted.org/packages/e2/5e/1fe4ea74f5c0afc681cbb1f34836fa251280c5aa3012dc803f6aac1382d6/openpyxl-3.2.0b1-py2.py3-none-any.whl#sha256=c9c32c7304ad9de30aa6632dd9836469fce0338e91f3e7875a1395f9163a3eec
Best match: openpyxl 3.2.0b1
Processing openpyxl-3.2.0b1-py2.py3-none-any.whl
Installing openpyxl-3.2.0b1-py2.py3-none-any.whl to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding openpyxl 3.2.0b1 to easy-install.pth file
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/openpyxl-3.2.0b1-py3.11.egg
Searching for latex2sympy2
Reading https://pypi.org/simple/latex2sympy2/
Downloading https://files.pythonhosted.org/packages/0c/9e/4520682ab29a9219f1845643fdc75f1453bebf4b602c6e4421579de1f05d/latex2sympy2-1.9.1-py3-none-any.whl#sha256=44f24d263d235164a91173167a30d449f4360e3f0a59239ce6b843c50a41c601
Best match: latex2sympy2 1.9.1
Processing latex2sympy2-1.9.1-py3-none-any.whl
Installing latex2sympy2-1.9.1-py3-none-any.whl to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding latex2sympy2 1.9.1 to easy-install.pth file
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/latex2sympy2-1.9.1-py3.11.egg
Searching for zstandard
Reading https://pypi.org/simple/zstandard/
Downloading https://files.pythonhosted.org/packages/a6/4c/63523169fe84773a7462cd090b0989cb7c7a7f2a8b0a5fbf00009ba7d74d/zstandard-0.24.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl#sha256=cd0d3d16e63873253bad22b413ec679cf6586e51b5772eb10733899832efec42
Best match: zstandard 0.24.0
Processing zstandard-0.24.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl
Installing zstandard-0.24.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding zstandard 0.24.0 to easy-install.pth file
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/zstandard-0.24.0-py3.11-linux-aarch64.egg
Searching for transformers-stream-generator
Reading https://pypi.org/simple/transformers-stream-generator/
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: stream-generator-0.0.1 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: generator-0.0.1 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: stream-generator-0.0.2 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: generator-0.0.2 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: stream-generator-0.0.3 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: generator-0.0.3 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: stream-generator-0.0.4 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: generator-0.0.4 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: stream-generator-0.0.5 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: generator-0.0.5 is an invalid version and will not be supported in a future release
  warnings.warn(
Downloading https://files.pythonhosted.org/packages/42/c2/65f13aec253100e1916e9bd7965fe17bde796ebabeb1265f45191ab4ddc0/transformers-stream-generator-0.0.5.tar.gz#sha256=271deace0abf9c0f83b36db472c8ba61fdc7b04d1bf89d845644acac2795ed57
Best match: transformers-stream-generator 0.0.5
Processing transformers-stream-generator-0.0.5.tar.gz
Writing /tmp/easy_install-y7r669kr/transformers-stream-generator-0.0.5/setup.cfg
Running transformers-stream-generator-0.0.5/setup.py -q bdist_egg --dist-dir /tmp/easy_install-y7r669kr/transformers-stream-generator-0.0.5/egg-dist-tmp-5dsxsrcb
/usr/local/python3.11.13/lib/python3.11/site-packages/setuptools/dist.py:771: UserWarning: Usage of dash-separated 'description-file' will not be supported in future versions. Please use the underscore name 'description_file' instead
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
zip_safe flag not set; analyzing archive contents...
Moving transformers_stream_generator-0.0.5-py3.11.egg to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding transformers-stream-generator 0.0.5 to easy-install.pth file
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/transformers_stream_generator-0.0.5-py3.11.egg
Searching for tqdm-multiprocess
Reading https://pypi.org/simple/tqdm-multiprocess/
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.1 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning:  is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.2 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.3 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.4 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.5 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.6 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.7 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.8 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.9 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.10 is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/local/python3.11.13/lib/python3.11/site-packages/pkg_resources/__init__.py:123: PkgResourcesDeprecationWarning: multiprocess-0.0.11 is an invalid version and will not be supported in a future release
  warnings.warn(
Downloading https://files.pythonhosted.org/packages/25/7e/0d889fc6c84e3df6b69aaafe893fc77f69b3d968ac9ce574d1c62c688050/tqdm_multiprocess-0.0.11-py3-none-any.whl#sha256=3ebdf03e7a675150fa0bbceaa9c3c64b8cb556e9ffafa4fe6c078e51820524aa
Best match: tqdm-multiprocess 0.0.11
Processing tqdm_multiprocess-0.0.11-py3-none-any.whl
Installing tqdm_multiprocess-0.0.11-py3-none-any.whl to /usr/local/python3.11.13/lib/python3.11/site-packages
Adding tqdm-multiprocess 0.0.11 to easy-install.pth file
Installed /usr/local/python3.11.13/lib/python3.11/site-packages/tqdm_multiprocess-0.0.11-py3.11.egg
Searching for pycocoevalcap

zstandard
transformers-stream-generator
tqdm-multiprocess
pycocoevalcap
