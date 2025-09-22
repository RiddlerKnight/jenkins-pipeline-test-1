# Jenkins Pipeline Test (TaskD)

## Questions

### 1. How did you test your pipelines?

1. create a jenkins instance from docker compose.\
   repo: <https://github.com/RiddlerKnight/jenkins-work>

2. Create Doxygen config then run test with GRPC repo that I was forked from so that I need to understand how it work.

3. Create Pipeline script (groovy file) and put the script through GUI.

4. Manually start the pipeline.

### 2. How did you test repoC python?

Same as the instruction above. For the python script, I have exported the log from the TaskB as an example. When it worked well, I put it in the groovy script.

---

### RepoA-doc contains binaries

They store architecture images and pdf files so that it is more convenient to read and versioning.

#### What is the advantage to use LFS?

LFS refers to Git Large File Storage.

Git can store not only code. It can store videos or binary files so that developers can work with big assets in the manner of version control style. \
Nowadays, I have seeing many developers use it to store the LLM/SLM model in git repository so that be convenient to use.

LFS help to efficiently handle the large files by separating LFS storage from code storage to keep repo lean.

Without LFS every clone or fetch pulls the full history of large files, it will slow down even if you don’t need them.

#### How to adjust this repository to support LFS?
