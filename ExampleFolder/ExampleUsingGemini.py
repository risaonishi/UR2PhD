# Since this file is in a different folder, we need to import sys then direct it
# to the folder that GoogleGemini.py is in
import sys
sys.path.append('../')
import GoogleGemini as gemini
import json # Only needed for this specific prompt to extract the dictionary from the response

def GetFuturesFromGPA(gpa: str, force=False) -> dict:
    "Return a dictionary of 3 possible jobs the given GPA can have with reasonings. jobsReasonsDict = {'job': 'reason', ...}"
    # Format a prompt using the given GPA
    prompt = f'Please tell me what future I can possibly have with a GPA of {gpa} in computer science. '
    prompt += 'Provide three separate answers along with a reason for each answer.  '
    prompt += 'If my GPA is below 2.0, simply output one answer of "hopeless" with a statement about how terrible my grades are. '
    prompt += 'Format your response as a Python dictionary, '
    prompt += 'where the keys are your answer, and the values are the reasonings.'

    # Get the response from Gemini
    response = gemini.AskGoogleGemini(prompt, force=force)

    # Return the response as a dictionary
    startIndex = response.find('{')
    endIndex = response.find('}') + 1
    response = response[startIndex:endIndex]
    jobsReasonsDict = json.loads(response)

    return jobsReasonsDict
    

def main():
    # Initialize Google Gemini first to load your Google credentials
    gemini.InitGoogleGemini()

    # Create a prompt to ask Google Gemini (Note how we can ask it to return Python-interpretable data structures)
    prompt = 'Please tell me what future I can possibly have with a GPA of 3.3 in computer science. '
    prompt += 'Provide three separate answers along with a reason for each answer.  '
    prompt += 'Format your response as a Python dictionary, '
    prompt += 'where the keys are your answer, and the values are the reasonings.'

    # Get the response from Google Gemini
    response = gemini.AskGoogleGemini(prompt)

    # Uncomment the following line to see the raw response
    #print(response)

    # Here Gemini is prompted to ouput a Python dictionary, so we can extract that
    startIndex = response.find('{') # Get rid of everything outside of the brackets
    endIndex = response.find('}') + 1
    response = response[startIndex:endIndex]
    jobsReasonsDict = json.loads(response) # JSON library can load strings as Python dictionaries or lists
    
    # Now we can do what we want, ex. just printing the potential jobs we can get:
    for job in jobsReasonsDict.keys():
        print(job)

    # We can output slightly nicer format:
    print('With a GPA of 3.3 one can potentially have the following future job:')
    for i, job in enumerate(jobsReasonsDict.keys()): # Enumerate lets you keep track of which loop iteration you are on
        print(f'Job #{i + 1}: {job}')
    print() # Prints empty line
    
    # We can automate this process if we want to process a batch of GPAs
    studentGpas = ['3.9', '2.2', '3.0', '1.0']
    for gpa in studentGpas:
        # Format everything above into a neat function
        jobsReasonsDict = GetFuturesFromGPA(gpa)
        
        # Output the results with some fancy print statements
        print(f'A student with a GPA of {gpa} can have the following future:')
        for k, (job, reason) in enumerate(jobsReasonsDict.items()): # Fancy but super useful loop through dictionary
            print()
            print(f'Job #{k + 1}: {job} || Reason: {reason}')
        print('=='*40)

if __name__ == '__main__':
    main()