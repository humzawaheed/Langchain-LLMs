modified:   My_Python_Files/main.py


# from langchain_community.llms import huggingface_endpoint
# from huggingface_hub import hf_api
# import os

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# llm = huggingface_hub.HuggingFaceHub(repo_id="finiteautomata/bertweet-base-sentiment-analysis",model_kwargs={"temperature":"0.5","max_length":"100"})
# llm = huggingface_endpoint.HuggingFaceEndpoint(huggingfacehub_api_token="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", repo_id="finiteautomata/bertweet-base-sentiment-analysis")

# input = llm("I love my dog!")

# response = llm(prompt=input)

# first_result = response[0]
# label = first_result["label"]
# score = first_result["score"]

# print(f"Label: {label}, Score: {score}")



# api = hf_api.HfApi()
# model_info = api.model_info("finiteautomata/bertweet-base-sentiment-analysis", token="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")
# print(model_info)
