# 导入依赖库
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# 加载 .env 文件中定义的环境变量
_ = load_dotenv(find_dotenv())

# 初始化 OpenAI 客户端
client = OpenAI()  # 默认使用环境变量中的 OPENAI_API_KEY 和 OPENAI_BASE_URL

# 基于 prompt 生成文本
def get_completion(prompt, model="gpt-3.5-turbo"):      # 默认使用 gpt-3.5-turbo 模型
    messages = [{"role": "user", "content": prompt}]    # 将 prompt 作为用户输入
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,                                  # 模型输出的随机性，0 表示随机性最小
    )
    return response.choices[0].message.content          # 返回模型生成的文本

# 任务描述
instruction = """
你的任务是识别用户对手机流量套餐产品的选择条件。
每种流量套餐产品包含三个属性：名称，月费价格，月流量。
根据用户输入，识别用户在上述三种属性上的倾向。
"""

# 用户输入
input_text = """
办个100G的套餐。
"""

# prompt 模版。instruction 和 input_text 会被替换为上面的内容
prompt = f"""
{instruction}

用户输入：
{input_text}
"""

# 调用大模型
response = get_completion(prompt)
print(response)