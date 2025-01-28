
---

# Document Management Application 📄

## Overview
This project is a **Streamlit-based application** for managing and exporting documents. It provides functionality for:
- Adding new records to a dataset.
- Filtering records based on user input.
- Exporting filtered records as PDFs.

The app is designed to streamline document management and provide an intuitive interface for users.

---

## Features
- **Add Records**: Input new data into the Excel dataset with dynamic fields.
- **Filter Records**: Filter data based on specific criteria to find relevant entries.
- **Export as PDF**: Generate and download populated PDFs for filtered records.
- **User-Friendly Interface**: Built with an attractive and responsive Streamlit UI.

---

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or later
- Pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/document-management-app.git
   cd document-management-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run main.py
   ```

---

## File Structure
```
.
├── main.py                       # Entry point for the Streamlit app
├── records.xlsx                  # Excel file for storing data
├── helper_functions/
│   ├── filter.py                 # Filtering logic
│   ├── input_fields.py           # Input field management
├── tabs/
│   ├── tab2.py                   # Logic for exporting PDFs
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## Usage

### 1. Add Records
- Navigate to the **Display Data** tab.
- Fill in the input fields and click **Submit** to add a new record to the dataset.

### 2. Filter Records
- Go to the **Export Documents** tab.
- Use the filter options to search for specific records.

### 3. Export PDFs
- Select the desired record(s) and click **Export PDF** to download the populated document.

---

## Technologies Used
- **Streamlit**: For building the web application.
- **Pandas**: For data manipulation.
- **pdfrw**: For working with PDF templates.
- **OpenPyXL**: For handling Excel files.

---

## Screenshots
### Main Page:
![Main Page](link-to-screenshot-1.png)

### Filter and Export:
![Filter Page](link-to-screenshot-2.png)

---

## Contributing
We welcome contributions! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- Thanks to the Streamlit community for their fantastic support.
- Icons used in the app are sourced from [Font Awesome](https://fontawesome.com).

---
