
import requests
import json

def get_form_question_answer_dict(jira_issue_id, api_base_url, api_token=None):
    """
    Fetches form data for a Jira issue, then fetches form details using the form id, and returns a dict mapping question labels to answers.
    Args:
        jira_issue_id (str): The Jira issue id.
        api_base_url (str): The base URL for the forms API.
        api_token (str, optional): API token for authentication, if required.
    Returns:
        dict: {question_label: answer}
    """
    headers = {"Authorization": f"Bearer {api_token}"} if api_token else {}
    # 1. Fetch the form for the issue id
    form_url = f"{api_base_url}/forms/{jira_issue_id}"
    resp = requests.get(form_url, headers=headers)
    resp.raise_for_status()
    form_data = resp.json()
    form_id = form_data.get("id")
    if not form_id:
        raise ValueError("Form ID not found in response.")

    # 2. Fetch the form details using the form id
    details_url = f"{api_base_url}/forms/details/{form_id}"
    details_resp = requests.get(details_url, headers=headers)
    details_resp.raise_for_status()
    details_data = details_resp.json()

    # 3. Build the question-to-answer dictionary
    questions = details_data["design"]["questions"]
    answers = details_data["state"]["answers"]
    qa_dict = {}
    for qid, qinfo in questions.items():
        key = qinfo.get("questionKey", qid)
        qtype = qinfo.get("type", "")
        answer = answers.get(qid)
        if answer is None:
            qa_dict[key] = None
        elif isinstance(answer, dict):
            if qtype == 'ts':
                # Text type
                qa_dict[key] = answer.get('text')
            elif qtype == 'cd':
                # Choice type, get value of first key pair from the list of choice
                choices = answer.get('choices', [])
                if choices and isinstance(choices, list):
                    # Find the label for the first choice id
                    choice_id = choices[0]
                    # Find the label from the question's choices list
                    choice_label = None
                    for c in qinfo.get('choices', []):
                        if c.get('id') == choice_id:
                            choice_label = c.get('label')
                            break
                    qa_dict[key] = choice_label if choice_label is not None else choice_id
                else:
                    qa_dict[key] = None
            elif 'text' in answer:
                qa_dict[key] = answer['text']
            elif 'choices' in answer:
                qa_dict[key] = answer['choices']
            elif 'files' in answer:
                qa_dict[key] = answer['files']
            else:
                qa_dict[key] = answer
        else:
            qa_dict[key] = answer
    return qa_dict

# Example usage with sample JSON file (for local testing):
def get_question_answer_dict_from_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    questions = data["design"]["questions"]
    answers = data["state"]["answers"]
    qa_dict = {}
    for qid, qinfo in questions.items():
        key = qinfo.get("questionKey", qid)
        qtype = qinfo.get("type", "")
        answer = answers.get(qid)
        if answer is None:
            qa_dict[key] = None
        elif isinstance(answer, dict):
            if qtype == 'ts':
                qa_dict[key] = answer.get('text')
            elif qtype == 'cd':
                choices = answer.get('choices', [])
                if choices and isinstance(choices, list):
                    choice_id = choices[0]
                    choice_label = None
                    for c in qinfo.get('choices', []):
                        if c.get('id') == choice_id:
                            choice_label = c.get('label')
                            break
                    qa_dict[key] = choice_label if choice_label is not None else choice_id
                else:
                    qa_dict[key] = None
            elif 'text' in answer:
                qa_dict[key] = answer['text']
            elif 'choices' in answer:
                qa_dict[key] = answer['choices']
            elif 'files' in answer:
                qa_dict[key] = answer['files']
            else:
                qa_dict[key] = answer
        else:
            qa_dict[key] = answer
    return qa_dict