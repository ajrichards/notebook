https://www.incredigeek.com/home/setting-up-databricks-dolly-on-ubuntu-with-gpu/

https://github.com/databrickslabs/dolly
https://huggingface.co/databricks/dolly-v2-3b
https://huggingface.co/databricks/dolly-v2-12b


Pre-reqs & setup
-------------------

1. ensure the nvidia-driver and nvidia-cuda-toolkit are installed

   ```bash
   ~$ nvidia-smi
   ```

2. be sure the environment is ready to go

   
   ```bash
   $ python -m venv env/dolly
   $ source env/dolly/bin/activate
   $ pip install -r requirements.txt
   ```
   
3. From a terminal run the following commands to initiate downloads

   >>> import torch
   >>> from transformers import pipeline
   >>> generate_text = pipeline(model="databricks/dolly-v2-12b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
   
>  Alternatively, If you want to use a smaller model run

>>>generate_text = pipeline(model="databricks/dolly-v2-3b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")

4. Test the prompt


>>> res = generate_text("Explain to me the difference between nuclear fission and fusion.")
>>> print(res[0]["generated_text"])
