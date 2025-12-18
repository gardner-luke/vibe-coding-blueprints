import subprocess
import os
import sys
import venv

def setup_virtualenv():
    """Create virtual environment for the future wind-farm-app"""
    venv_dir = ".venv"
    
    if os.path.isdir(venv_dir):
        print(f"✓ Virtual environment already exists at {venv_dir}")
        return
    
    print("=" * 60)
    print("Creating Python virtual environment for app development...")
    print("=" * 60)
    print(f"Creating virtual environment in {venv_dir}...")
    
    try:
        venv.create(venv_dir, with_pip=True)
        print("✓ Virtual environment created successfully")
        print(f"✓ You can activate it later with:")
        if sys.platform == "win32":
            print(f"   {venv_dir}\\Scripts\\activate")
        else:
            print(f"   source {venv_dir}/bin/activate")
    except Exception as e:
        print(f"Warning: Failed to create virtual environment: {e}")
        print("You can create it manually later if needed.")
    
    print("=" * 60)
    print()

def load_config(config_path="config.yaml"):
    """Simple YAML parser for flat key-values to avoid dependencies"""
    config = {}
    try:
        with open(config_path, "r") as f:
            for line in f:
                # Remove comments and whitespace
                line = line.split("#")[0].strip()
                if not line or ":" not in line:
                    continue
                
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip().strip('"\'')
                
                # Only care about top-level keys for now
                if key not in config:
                    config[key] = val
        return config
    except FileNotFoundError:
        print(f"Error: {config_path} not found.")
        sys.exit(1)

def run_command(cmd, cwd=None, suppress_output=False):
    print(f"Running: {' '.join(cmd)}")
    
    if suppress_output:
        print("Job is running... This may take a minute or two.", flush=True)

    if suppress_output:
        # Capture output, but print URLs if found
        process = subprocess.Popen(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, # Merge stderr into stdout
            text=True,
            bufsize=1
        )
        
        full_output = []
        for line in process.stdout:
            full_output.append(line)
            # Check for URLs in the output
            if "https://" in line or "View run" in line:
                print(line.strip())
        
        process.wait()
        
        if process.returncode == 0:
            print("SUCCESS")
        else:
            print(f"Command failed with exit code {process.returncode}")
            print("".join(full_output))
            sys.exit(process.returncode)
    else:
        try:
            subprocess.run(cmd, cwd=cwd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with exit code {e.returncode}")
            sys.exit(e.returncode)

def main():
    # Step 1: Set up virtual environment for future app development
    setup_virtualenv()
    
    # Step 2: Load configuration
    config = load_config()
    
    required_vars = ["catalog", "schema"]
    missing = [v for v in required_vars if v not in config]
    
    if missing:
        print(f"Error: Missing required variables in config.yaml: {', '.join(missing)}")
        sys.exit(1)
        
    catalog = config["catalog"]
    schema = config["schema"]
    
    bundle_dir = "fsa_env_setup"
    if not os.path.isdir(bundle_dir):
        print(f"Error: Directory {bundle_dir} not found.")
        sys.exit(1)

    # Step 3: Deploy data bundle
    print(f"Deploying data bundle using Catalog: {catalog}, Schema: {schema}...")
    
    # Deploy bundle
    run_command([
        "databricks", "bundle", "deploy",
        "--var", f"catalog={catalog}",
        "--var", f"schema={schema}"
    ], cwd=bundle_dir)
    
    # Run load_data_job
    print("\nRunning load data job...")
    run_command([
        "databricks", "bundle", "run", "load_data_job",
        "--var", f"catalog={catalog}",
        "--var", f"schema={schema}"
    ], cwd=bundle_dir, suppress_output=True)
    
    print("\n✅ Data setup complete! You are ready to proceed to Step 3: Build the App with AI.")

if __name__ == "__main__":
    main()

