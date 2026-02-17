# Context Generator

The Context Generator is a tool designed to scrape environment data and project state into a consolidated Markdown file. It utilizes Jinja2 templates to combine shell command outputs, file contents, and structured YAML data into a final document.

## Setup

* **Python**: 3.9+ recommended.
* **Dependencies**: Install the required libraries via `pip install -r requirements.txt`.
    * `jinja2`: Template engine.
    * `PyYAML`: YAML parser.

### Environment 

The script executes shell commands and API calls that may require authentication. Ensure the following variables are set in your session:

```bash
export MSSQL_USER="<mssql-user>"
export MSSQL_PASSWORD="<mssql-password>"
export JENKINS_USERNAME="<username>"
export JENKINS_PASSWORD="<password>"
export ARTIFACTORY_USERNAME="<username>"
export ARTIFACTORY_PASSWORD="<password>"
```

### Git

In addition, the following repositories from the github must be cloned locally and configured,

- Clone the entire github project into a folder. Adjust the `properties.tools.github.` property to match your local directory.

## Configuration Files

The generator relies on three primary configuration files to determine what data is collected:

1. **`task.yaml` (The "What")**: The primary user-facing file. It defines which components (Inventory, Tools, Docs) and specific "views" are enabled for the current task.
2. **`config/props.yaml` (The "Where")**: Contains environment-specific properties such as base URLs, filesystem paths, and default usernames.
3. **`config/views.yaml` (The "How")**: Maps view names to technical implementations. This is where shell commands (e.g., `kubectl get pods`) or file mappings are defined.

## Templating Engine

The generator extends standard Jinja2 with custom functions to facilitate data collection:

* **`command(str)`**: Executes a shell command on the local machine and returns the result as a string. For remote data, templates often wrap this in `ssh` or `curl` calls.
* **`file(path)`**: Reads the content of a file from the local filesystem.
* **`load(path)`**: Parses a YAML file into a dictionary for use within the template context.

### Security Warning

This tool enables **Arbitrary Code Execution (ACE)** by design via the `command` function to capture environment state. Only render templates and configuration files from trusted sources. Do not run the script in environments where untrusted users can modify the YAML configurations or Jinja2 templates.

## Usage

Run the generator from the `task/` directory:

```bash
python main.py [template_file] [-o output_file] [-v vars_file]
```

* **`template_file`**: The entry point Jinja2 template (Default: `task.md.j2`).
* **`-o, --output`**: The destination path for the rendered Markdown (Default: `prompt/prompt.md`).
* **`-v, --vars`**: Path to a specific task YAML file (Default: `task.yaml`).

### Parameters

Some blocks in the `task.yml` have parameters. These parameters are ingested by the views to dynamically modify the generated context. 

The *scope* of parameters extends down the task tree, but not up. In other words, `parameters` defined under `task.inventory.host.parameters` are not shared by `parameters` defined under the `task.inventory.local.parameters`.