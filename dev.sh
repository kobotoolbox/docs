echo "Creating virtual environment…"
python -m venv koboenv
echo "Activating virtual environment…"
source koboenv/bin/activate
echo "Virtual environment ready ✓"

echo "Installing Python dependencies…"
pip install -r requirements.txt
echo "Installing Node dependencies…"
npm install
echo "Dependencies ready ✓"

echo "Building Sphinx…"
make html
echo "Shpinx ready ✓"

echo "Opening project in the browser…"
open _build/html/index.html
