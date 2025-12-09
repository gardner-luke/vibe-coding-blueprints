# fsa_env_setup

## Getting Started

1. Clone this repository and navigate to it:
   ```bash
   git clone <repo-url>
   cd fsa_env_setup
   ```

2. Install the Databricks CLI: https://docs.databricks.com/dev-tools/cli/install.html

3. Authenticate to your Databricks workspace:
   ```bash
   databricks configure
   ```

4. Deploy the bundle (specify your catalog and schema):
   ```bash
   databricks bundle deploy --var="catalog=my_catalog" --var="schema=my_schema"
   ```

5. Run the job:
   ```bash
   databricks bundle run load_data_job --var="catalog=my_catalog" --var="schema=my_schema"
   ```

## Resources

- [Databricks Asset Bundles documentation](https://docs.databricks.com/dev-tools/bundles/index.html)
- [Databricks CLI documentation](https://docs.databricks.com/dev-tools/cli/index.html)
