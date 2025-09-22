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
Nowadays, I have seeing many developers use it to store the LLM/SLM models in git repository so that be convenient to use.

LFS help to efficiently handle the large files by separating LFS storage from code storage to keep repo lean with lightweight pointer inside the Git repo.

Without LFS every clone or fetch pulls the full history of large files, it will slow down even if you don’t need them.

#### How to adjust this repository to support LFS?

1. Install git-lfs in to your PC

2. Add LFS tracking rules

Decide which files belong in LFS (by extension or path), then create/update `.gitattributes`

Create `.gitattributes` then define the rules.

```text
# From the repo root
git lfs track "*.psd"
git lfs track "*.zip"
git lfs track "*.mp4"
git lfs track "assets/binaries/**"
```

commit the `.gitattributes` file.

```bash
git add .gitattributes
git commit -m "Enable Git LFS for large/binary assets"
```

then commit large files as usual

```bash
git add path/to/large-file.mp4
git commit -m "Add video asset via LFS"
git push
```
