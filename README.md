- python version 3.11.8 (3.12 버전은 오류 발생)

- 모델 설치 방법
    - sudo apt install git-lfs
    - git lfs install
- 모델 정보
    - git clone https://huggingface.co/openai-community/gpt2
    - llama model download --source huggingface --model-id meta-llama/Llama-2-7b-c --hf-token TOKEN
    - llama model download --source huggingface --model-id meta-llama/Llama-2-7b-chat --hf-token TOKEN
    '''
    python convert_llama_weights_to_hf.py \
      --input_dir /path/to/original/checkpoints \
      --output_dir /path/to/hf-format-model \
      -- model_size 7B
    '''