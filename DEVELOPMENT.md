# Development reference

To run `route53-ddns` locally:

```bash
python src/route53_ddns/cli.py --zone ecarlesso.net --record hom
```

## Run Tests and Coverage

```bash
# Runs the coverage
coverage run -m pytest
# Shows the report
coverage report
# Generate HTML report
coverage html -d coverage_html_report
```

## Publish a new version:

```bash
# Will generate the artifacts
python -m build
# Will upload them to pypi. Credentials are read from ~/.pypirc
python3 -m twine upload  dist/*
```
