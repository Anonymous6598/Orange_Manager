import openvino_genai

class LargeLanguageModel:
    def __init__(self):
        self.language_model = "Llama-3.2-1B-Instruct"
        self.device = "NPU"

    def init_model(self):
        pipeline_config = {f"GENERATE_HINT": f"BEST_PERF"}
        pipe: openvino_genai.LLMPipeline = openvino_genai.LLMPipeline(self.language_model, self.device, pipeline_config)
        return pipe

    def ResponseFromAI(self, prompt, pipe):
        config: openvino_genai.GenerationConfig = openvino_genai.GenerationConfig()
        config.max_new_tokens = 1024
        config.temperature = 0.3
        config.top_p = 0.5
        config.top_k = 1
        config.repetition_penalty = 1.0
        config.num_return_sequences = 1
        config.num_beams = 1
        config.num_return_sequences = 1
        config.do_sample = False
        config.eos_token_id = -1

        result: str = pipe.generate(prompt, config)
        return result