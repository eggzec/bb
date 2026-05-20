# Installation

## Install the package

=== "uv"

    ```bash
    uv add bb
    ```

=== "pip"

    ```bash
    pip install bb
    ```

## Development install

```bash
git clone https://github.com/your-org/bb.git
cd bb
uv sync
```

## Environment variables

Set these variables before running any SDK code. Which variables are required depends on which target you are using.

| Variable | Required for | Description |
|---|---|---|
| `BB_TOKEN` | Cloud | Atlassian API token from `id.atlassian.com/manage-profile/security/api-tokens` |
| `BB_WORKSPACE` | Cloud (optional) | Default workspace slug — avoids passing `workspace=` on every call |
| `BB_DC_TOKEN` | DC (token auth) | Bitbucket Data Center personal access token |
| `BB_DC_BASE_URL` | DC | Data Center REST API base URL, e.g. `https://bitbucket.example.com/rest` |
| `BB_DC_USERNAME` | DC (basic auth) | Username for HTTP Basic authentication |
| `BB_DC_PASSWORD` | DC (basic auth) | Password for HTTP Basic authentication |

!!! note "DC authentication"
    For Data Center, use either token auth (`BB_DC_TOKEN` + `BB_DC_BASE_URL`) or basic auth (`BB_DC_USERNAME` + `BB_DC_PASSWORD` + `BB_DC_BASE_URL`). `BB_DC_BASE_URL` is required for both methods.

### Example: Cloud

```bash
export BB_TOKEN=your_atlassian_api_token
export BB_WORKSPACE=myworkspace      # optional
```

### Example: Data Center (token auth)

```bash
export BB_DC_TOKEN=your_personal_access_token
export BB_DC_BASE_URL=https://bitbucket.example.com/rest
```

### Example: Data Center (basic auth)

```bash
export BB_DC_USERNAME=youruser
export BB_DC_PASSWORD=yourpassword
export BB_DC_BASE_URL=https://bitbucket.example.com/rest
```
