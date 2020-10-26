<h1>Virtual Environments Notes</h1>

<ol>
	<li>
		<h2>Create a virtual Environment:</h2>
		python -m venv <environment name>
	</li>
	<li>
		<h2>Activate a Virtual Environment</h2>
		<environment name>/scripts/activate
	</li>
	<li>
		<h2>Deactivate a Virtual Environment</h2>
		deactivate
	</li>
	<li>
		<h2>Delete a Virtual Environment</h2>
		remove the <environment name> directory
	</li>
	<li>
		<h2>List Installed Packages</h2>
		pip list
	</li>
	<li>
		<h2>Install a Package</h2>
		pip install <package name>
	</li>
	<li>
		<h2>Generate requirements.txt</h2>
		pip freeze
		copy output to requirements.txt
	</li>
	<li>
		<h2>Install from requirments.txt</h2>
		pip install -r requirements.txt
	</li>		
</ol>

