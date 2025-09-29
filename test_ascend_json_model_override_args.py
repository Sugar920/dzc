import unittest
from types import SimpleNamespace

import requests

from sglang.srt.utils import is_npu, kill_process_tree
from sglang.test.run_eval import run_eval
from sglang.test.test_utils import (
    DEFAULT_SMALL_MODEL_NAME_FOR_TEST,
    DEFAULT_TIMEOUT_FOR_SERVER_LAUNCH,
    DEFAULT_URL_FOR_TEST,
    CustomTestCase,
    popen_launch_server,
)


class TestJsonModelOverrideArgs(CustomTestCase):
    model = "/root/.cache/modelscope/hub/models/LLM-Research/Llama-3.2-1B-Instruct" if is_npu() else model = DEFAULT_SMALL_MODEL_NAME_FOR_TEST
    base_url = DEFAULT_URL_FOR_TEST

    @classmethod
    def setUpClass(cls):
        other_args = [
          "--trust-remote-code",
          "--enable-multimodal",
          "--mem-fraction-static",
          "0.8",
          "--attention-backend",
          "ascend",
          "--disable-cuda-graph",
          "--json-model-override-args",
          '{"max_position_embeddings": 5}',
        ]
        cls.process = popen_launch_server(
          cls.model,
          cls.base_url,
          timeout=DEFAULT_TIMEOUT_FOR_SERVER_LAUNCH,
          other_args=other_args,
        )

    @classmethod
    def tearDownClass(cls):
        kill_process_tree(cls.process.pid)

    def test_json_model_override_args(self):
        response = requests.get(f"{DEFAULT_URL_FOR_TEST}/health_generate")
        self.assertEqual(response.status_code, 200)

        response = requests.post(
            f"{DEFAULT_URL_FOR_TEST}/generate",
            json={
                "text": "The ancient Romans made significant contributions to various fields, including law, philosophy, science, and literature. They were known for their engineering achievements, such as the construction of the Colosseum and the Pantheon. Their art and architecture were also highly esteemed, with the Colosseum being a symbol of their power and influence. In science, they made important contributions to astronomy and mathematics. Literature was also a major part of their culture, ",
                "sampling_params": {
                    "temperature": 0,
                    "max_new_tokens": 32,
                },
            },
        )
      print(reponse.json()) 
        # self.assertEqual(response.status_code, 200)
        # self.assertIn("Paris", response.text)


if __name__ == "__main__":
    unittest.main()
