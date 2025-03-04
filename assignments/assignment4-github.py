# Libraries
import requests
import json
from config import config
from github import Github

# Read in the contnts of the my private repository using requests and a key
url = "https://api.github.com/repos/a-o-connor/example_private_repo/contents"
api_key = config["githubtoken"] #API key is defined in a dict object the file config.py, which is listed in Gitignore and does not get pushed to Github
response = requests.get(url, auth = ("token", api_key))
repo_json = response.json() #returns a json object with details of the repo contents, if the keys works! 

docnames = [] #Initialise an empty list to save the file names in the repo to
for i in range(0, len(repo_json)): #For each document listed in the repo json...
    docnames.append(repo_json[i]["name"]) #...read in the file name and add it to the docnames list 

filename = docnames[2] #Files 0 and 1 are gitignore and readme, I want to edit the first file in the repository that is not these

# Using the PyGithub extension to edit the file: 
g = Github(api_key) # Initialize a GitHub instance using the github token read in from config file earlier. 

repo = g.get_repo("a-o-connor/example_private_repo") #Access the example private repository made for this assignment
file = repo.get_contents(filename) #Get the contents of the file defined earlier as filename

file_url = file.download_url #Get the download URL for the file 

response = requests.get(file.download_url) #Download this URL using the get from requests package

file_content = response.text #This should return the ctext contents of the file
# print(file_content)

updated_file_contents = file_content.replace("Andrew", "Ailsa") #This takes the string of text read in with file content and replaces all instance of the word Andrew with Ailsa


repo.update_file(file.path, "Replacing all instances of Andrew with my name", updated_file_contents, file.sha) #This update_file function is from the Pygithub documentation:
#Reference https://pygithub.readthedocs.io/en/stable/github_objects/Repository.html#github.Repository.Repository.update_file