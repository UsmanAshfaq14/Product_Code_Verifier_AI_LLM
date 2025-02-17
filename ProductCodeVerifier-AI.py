import json
import csv
from typing import Dict, List, Union
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProductRecord:
    product_id: str
    product_code: str
    status: str = "Clear"
    
class ProductCodeVerifier:
    def __init__(self):
        self.products: List[ProductRecord] = []
        self.validation_errors: List[str] = []
        
    def load_data(self, data: Union[str, Dict], format_type: str = "json") -> bool:
        """Load and validate input data in either JSON or CSV format."""
        try:
            if format_type.lower() == "json":
                if isinstance(data, str):
                    data = json.loads(data)
                for product in data.get("products", []):
                    self.products.append(
                        ProductRecord(
                            product_id=product.get("product_id", ""),
                            product_code=product.get("product_code", "")
                        )
                    )
            elif format_type.lower() == "csv":
                csv_data = csv.DictReader(data.splitlines())
                for row in csv_data:
                    self.products.append(
                        ProductRecord(
                            product_id=row.get("product_id", ""),
                            product_code=row.get("product_code", "")
                        )
                    )
            return True
        except Exception as e:
            self.validation_errors.append(f"ERROR: Invalid data format - {str(e)}")
            return False

    def validate_data(self) -> bool:
        """Validate the loaded data against the required rules."""
        is_valid = True
        
        for product in self.products:
            if not product.product_id:
                self.validation_errors.append("ERROR: Missing required field: product_id")
                is_valid = False
            if not product.product_code:
                self.validation_errors.append("ERROR: Missing required field: product_code")
                is_valid = False
            if not isinstance(product.product_code, str):
                self.validation_errors.append("ERROR: Invalid data type for field: product_code")
                is_valid = False
                
        return is_valid

    def check_palindromes(self):
        """Check each product code for palindromes."""
        for product in self.products:
            if product.product_code == product.product_code[::-1]:
                product.status = "Flagged"

    def generate_report(self) -> str:
        """Generate a detailed markdown report of the analysis."""
        report = []
        
        # Data Validation Report
        report.append("# Data Validation Report\n")
        
        report.append("## 1. Data Structure Check:")
        report.append(f"- Number of products: {len(self.products)}")
        report.append("- Number of fields per product: 2\n")
        
        report.append("## 2. Required Fields Check:")
        report.append("- product_id: Present")
        report.append("- product_code: Present\n")
        
        report.append("## 3. Data Type Validation:")
        report.append("- product_code (string): Validated\n")
        
        if not self.validation_errors:
            report.append("## Validation Summary:")
            report.append("Data validation is successful! Proceeding with analysis...\n")
        else:
            report.append("## Validation Errors:")
            for error in self.validation_errors:
                report.append(f"- {error}\n")
        
        # Formulas Used
        report.append("# Formulas Used:")
        report.append("1. String Reversal Formula:")
        report.append("   $$")
        report.append("   \\text{reversed\\_code} = \\text{reverse(product\\_code)}")
        report.append("   $$\n")
        
        # Product Analysis
        report.append("# Product Code Analysis")
        report.append(f"Total Products Evaluated: {len(self.products)}\n")
        
        report.append("# Detailed Analysis\n")
        for product in self.products:
            report.append(f"## Product {product.product_id}")
            report.append("### Input Data:")
            report.append(f"- Product Code: {product.product_code}\n")
            
            report.append("### Detailed Steps:")
            report.append(f"1. **Original Product Code:** {product.product_code}")
            report.append("2. **Reversal Process:**")
            report.append("   - Step-by-step: Reverse the string character by character.")
            report.append(f"   - Example: IF {product.product_code} = \"{product.product_code}\", "
                         f"THEN \"reversed_code\" = \"{product.product_code[::-1]}\".")
            report.append("3. **Comparison:**")
            report.append("   - IF original product code equals reversed code, THEN mark as \"Flagged\" (palindrome detected).")
            report.append("   - ELSE, mark as \"Clear\" (not a palindrome).\n")
            
            report.append(f"### Final Status: {product.status}")
            explanation = ("This product code is a palindrome (reads the same forwards and backwards)." 
                         if product.status == "Flagged" 
                         else "This product code is not a palindrome.")
            report.append(f"Explanation: {explanation}\n")
        
        # Flagged List
        flagged_products = [p for p in self.products if p.status == "Flagged"]
        report.append("# Flagged List:")
        if flagged_products:
            for product in flagged_products:
                report.append(f"- Product ID: {product.product_id}, Code: {product.product_code}")
        else:
            report.append("No palindrome product codes detected.")
        
        return "\n".join(report)

def main():
    # Example usage
    json_data = """
    {
    "products": [
        {"product_id": "P001", "product_code": "SAGAS"},
        {"product_id": "P002", "product_code": "REVIVER"},
        {"product_id": "P003", "product_code": "EXAMPLE"},
        {"product_id": "P004", "product_code": "ROTATOR"},
        {"product_id": "P005", "product_code": "PYRAMID"},
        {"product_id": "P006", "product_code": "LEVELS"},
        {"product_id": "P007", "product_code": "ORIENTAL"},
        {"product_id": "P008", "product_code": "DECODED"},
        {"product_id": "P009", "product_code": "REPAPER"},
        {"product_id": "P010", "product_code": "INNOVATE"},
        {"product_id": "P011", "product_code": "KAYAKS"},
        {"product_id": "P012", "product_code": "ANNA"},
        {"product_id": "P013", "product_code": "STATISTICS"},
        {"product_id": "P014", "product_code": "RACECARX"},
        {"product_id": "P015", "product_code": "MALAYALAMX"}
    ]
    }

    """
    
    verifier = ProductCodeVerifier()
    if verifier.load_data(json_data):
        if verifier.validate_data():
            verifier.check_palindromes()
            report = verifier.generate_report()
            print(report)
        else:
            print("Validation failed. Please check the errors and try again.")
    else:
        print("Failed to load data. Please check the format and try again.")

if __name__ == "__main__":
    main()