from src.llm_client import generate_response         # pass only prompts
from src.read_prompts import load_prompt             # pass only file path that want to load
from src.resume_to_text_clean import text_extract    # pass resume path for text extract

def main():
    print("======Wellcome in AI Interview Assitance ====== ")
    resume=input("Enter your resume path (resume must be in pdf) \n")
    resume_text=text_extract(resume)
    
    prompt_templete=load_prompt("prompts/interviewer.txt")
    model_prompt=prompt_templete.format(resume=resume_text)

    # print(resume_text)

    history = [
    {"role": "user", "content": model_prompt}
    ]

    first_question = generate_response(history)

    print("\n")
    print(first_question)

    history.append(
        {"role": "assistant", "content": first_question}
    )

    while True:

        answer = input("\nYour Answer: ")

        if answer.lower() == "end interview":
            break

        history.append(
            {"role": "user", "content": answer}
        )

        response = generate_response(history)

        print("\n")
        print(response)

        history.append(
            {"role": "assistant", "content": response}
        )

    print("\nInterview Ended")

if __name__ == "__main__":
    main()
