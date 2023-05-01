from llmagent.language_models.openai_gpt import OpenAIGPT, OpenAIGPTConfig


def test_openai_gpt():
    cfg = OpenAIGPTConfig(
        type="openai",
        max_tokens=100,
        chat_model="gpt-3.5-turbo",
        completion_model="text-davinci-003",
    )

    mdl = OpenAIGPT(config=cfg)

    question = "What is the capital of france?"

    response = mdl.generate(prompt=question, max_tokens=10)
    assert "Paris" in response.message

    messages = [
        dict(role="system", content="You are a helpful assitant"),
        dict(role="user", content=question),
    ]
    response = mdl.chat(messages=messages, max_tokens=10)
    assert "Paris" in response.message
