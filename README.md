# Assignment: ASSIGNMENT NAME

This repository is compatible with [Replit](https://replit.com/).

## Materials within this repo

There are few major files here.

- `main.py` is the main code base file. It will be used to complete
  the assignment by students.
- `tests` directory is the home of **all** tests provided for the assignment.
- `.lesson` directory is the documentation source
    - `.lesson/instructions.md` is the assignment instructions file visible for
      all.
    - `.lesson/lessonplan.md` is the private file, available only for
      the assignment owners and/or admins. Do not add solution to this file.
      Use it for notes for the assignment.
    - `.lesson/assets` is the home for all static files required by the docs.

Other documents may be included into `.lesson` directory.
Only `instructions.md` will be visible for the students.

This repository stores its own **assets** within `.lesson` directory as well.

## Set up assignment repository

### Creating a new repository from template

Press the `Use this template` green button at the top.

![](.lesson/assets/replit/repo-from-template.png)

This will lead you to the repository creation page.
Provide a valid meaningful repo name and add its description.

There is no need to clone branches except `master`. Default branch is always at
the most stable version.

### Protect master branch

It's important not to work within the default branch. So, ensure noone can
commit directly into `master`. In **Settings** navigate to **Branches** under
the **Code and automation** section. Press `Add branch protection rule` button.

![](.lesson/assets/replit/branch-protection-1.png)

Provide branch name pattern and check following options:

- **Require a pull request before merging**
- **Require status checks to pass before merging**
    - **Require branches to be up date before merging**
- **Do not allow bypassing the above settings**

![](.lesson/assets/replit/branch-protection-2.png)
![](.lesson/assets/replit/branch-protection-3.png)
![](.lesson/assets/replit/branch-protection-4.png)

This will protect the default branch from committing directly into it.
You may apply other protection rules, in case of need.

Create a branch protection rule.

## Getting started

1. Clone your assignment repo to your local machine.
2. Create a new topic branch (e.g. `feature/assignment`).
3. Complete the assignment instructions. Provide a clear objective and usage
   examples.
4. Prepare the code boilerplate file (`main.py`).
5. Add test cases (use `unittest` framework only).

### Make your boilerplate file invisible for Git

When a boilerplate code is ready, you may want to implement the actual logic
for the assignment. It's useful for running tests especially. However, you do
not want to put the implementation to the assignment repository.

To make changes inside a file invisible for Git use:

```shell
git update-index --assume-unchanged <file>
```

To switch it back:

```shell
git update-index --no-assume-unchanged <file>
```

Always do this while working with non-boilerplate code inside `main.py`.

### Testing

Assignment follows TDD approach. This means all the tests should fail.
Decorate your test cases with `unittest.expectedFailure`. Otherwise, it
will be impossible to merge topic branch into `master.`

## Add the assignment to Replit

There is no way to import GitHub repo as lesson project to Replit. So, it's
a little bit tricky to connect the Replit project with a GitHub repository.

Navigate to EDU organization's team and press `Create project` button.

![](.lesson/assets/replit/replit-create-project-1.png)

Provide all the information about the assignment.

![](.lesson/assets/replit/replit-create-project-2.png)

There is an [assignments library](https://replit.com/@assignments-library)
of current course available on Replit. For the assignments within this team,
there is no need to set a **due date**. Assignments will be copied to other
working teams from here.

In the repl, first press `Add lesson contents` button. Replit does not remove
it, until it hasn't been clicked. And this may be annoying to see it each time.
After that open `Git` tab, by pressing the corresponding button inside
**Tools** section.

![](.lesson/assets/replit/repl-configure-1.png)

On `Git` tab **uncheck** "Create initial commit with all changes" option.
The GitHub repo is the only source of any changes for the assignment. After
that press `Initialize Git Repository`.

![](.lesson/assets/replit/repl-configure-2.png)

On `Git` tab press `Reset All` button. Approve discard changes actions.

![](.lesson/assets/replit/repl-configure-3.png)

In the **Tools** section press `Shell` button to access the shell.
Add remote repository as common. Note, it may be tricky to use SSH access.
Any way, HTTP will be quite enough until you aren't going to use Replit for
the assignment preparation works. After that `fetch` all the changes and
switch to `master` branch.

```shell
git remote add origin <remote_repo_url>
git fetch
git switch master
```

The repl set up is complete at this point.

### Add Replit project tests

In **Tools** section press `Tests` button and choose a testing method,
*Unit tests* will be suitable in most cases.

![](.lesson/assets/replit/repl-configure-4.png)

First you need to set up unit tests. In a setup window add required imports.
Also, you can provide `setUp` and `tearDown` methods within advanced setup
section.

![](.lesson/assets/replit/repl-configure-5.png)

After the `unittest` framework is set up, it a copy-paste time. Add tests by
pressing `Add test` button. Provide a test name (omit "test" at the beginning),
error message and the test's code itself.
Press `Create test` button when ready.

![](.lesson/assets/replit/repl-configure-6.png)

## Providing a solution for students

On the repls overview page, press "three-dots" button on a repl and select
`Create solution` option.

![](.lesson/assets/replit/repl-create-solution-1.png)

This will create a new repl, there you may provide the solution. Once you're
done - press `Create/Update solution` button in the top-right corner. Set up
when the solution is available for the students.

![](.lesson/assets/replit/repl-create-solution-2.png)

## Publish the assignment

When the assignment is ready, simply check `Published`. Alternatively, you may
press `Publish project` button in the top-right corner of the Repl page.

![](.lesson/assets/replit/repl-publish.png)

`Published` flag is used to track assignment that are ready.

### Assignment pre-publish check list

- [ ] Instructions are included to the repl
- [ ] Tests are configured properly 
- [ ] Check tests are failed for the assignment
- [ ] Solution provided
- [ ] Check tests are passing for the solution
- [ ] pyproject file is updated
- [ ] Instructions are included to the repl
- [ ] Tests are configured properly 
- [ ] Check tests are failed for the assignment
- [ ] Solution provided
- [ ] Check tests are passing for the solution
