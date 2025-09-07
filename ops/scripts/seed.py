import sys
import os

sys.path.insert(0, '/app')
sys.path.insert(0, '/')

from app.db.session import SessionLocal
from app.models.credit_bureau import CreditBureau
from app.models.creditor import Creditor

def seed_data():
    db = SessionLocal()
    try:
        # Seed Credit Bureaus
        bureaus = [
            {"name": "Equifax", "website": "https://www.equifax.com"},
            {"name": "Experian", "website": "https://www.experian.com"},
            {"name": "TransUnion", "website": "https://www.transunion.com"},
        ]
        for bureau_data in bureaus:
            bureau = db.query(CreditBureau).filter_by(name=bureau_data["name"]).first()
            if not bureau:
                db.add(CreditBureau(**bureau_data))

        # Seed Creditors
        creditors = [
            {"name": "Capital One", "address": "1680 Capital One Dr, McLean, VA 22102"},
            {"name": "Chase", "address": "270 Park Ave, New York, NY 10017"},
            {"name": "Bank of America", "address": "100 N Tryon St, Charlotte, NC 28255"},
            {"name": "Wells Fargo", "address": "420 Montgomery St, San Francisco, CA 94104"},
            {"name": "Citibank", "address": "399 Park Ave, New York, NY 10022"},
        ]
        for creditor_data in creditors:
            creditor = db.query(Creditor).filter_by(name=creditor_data["name"]).first()
            if not creditor:
                db.add(Creditor(**creditor_data))

        db.commit()
        print("Seed data for credit bureaus and creditors has been added.")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
