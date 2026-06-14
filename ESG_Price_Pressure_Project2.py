
# STEP 1: CONSTRUCT THE DATASET (THE BIG FOUR)

# Data points represent estimated industry averages for ESG performance,
# revenue size (in billions USD), and baseline cost of capital.

big_four = [
    {
        "Firm": "Deloitte",
        "ESG_Score": 88,          # High focus on green tech transformation
        "Revenue_Billions": 65.0,
        "Base_Cost_of_Capital": 0.075  # 7.5% fundamental cost to borrow/invest
    },
    {
        "Firm": "PwC",
        "ESG_Score": 82,          # Strong net-zero carbon commits
        "Revenue_Billions": 53.0,
        "Base_Cost_of_Capital": 0.075
    },
    {
        "Firm": "EY",
        "ESG_Score": 79,          # Focus on sustainable supply chain consulting
        "Revenue_Billions": 51.0,
        "Base_Cost_of_Capital": 0.078
    },
    {
        "Firm": "KPMG",
        "ESG_Score": 71,          # Solid ESG framework, slightly smaller scale
        "Revenue_Billions": 36.0,
        "Base_Cost_of_Capital": 0.080
    }
]


# STEP 2: QUANTIFY ESG PRICE PRESSURE

# Academic Theory: Higher ESG scores apply downward pressure on borrowing costs,
# artificially inflating the "implied valuation" of the firm's internal assets.

print("QUANTIFYING ESG PRICE PRESSURE AND DISTORTIONS")

for firm in big_four:
    # 1. Calculate Interest Rate Discount (Price Pressure)
    # Firms with ESG scores over 75 get a borrowing discount due to "green demand"
    if firm["ESG_Score"] > 75:
        esg_discount = (firm["ESG_Score"] - 75) * 0.0005  # 0.05% discount per point
    else:
        esg_discount = 0.0
        
    firm["Actual_Cost_of_Capital"] = firm["Base_Cost_of_Capital"] - esg_discount
    
    # 2. Calculate Asset Valuation Distortion
    # A lower cost of capital artificially inflates asset value. 
    # Using a standard perpetuity formula: Value = Revenue / Cost of Capital
    fundamental_value = firm["Revenue_Billions"] / firm["Base_Cost_of_Capital"]
    distorted_value = firm["Revenue_Billions"] / firm["Actual_Cost_of_Capital"]
    
    firm["Valuation_Distortion_Pct"] = ((distorted_value - fundamental_value) / fundamental_value) * 100


# STEP 3: OUTPUT COMPANY ANALYSIS & RESULTS

for firm in big_four:
    print(f"\nFirm: {firm['Firm']}")
    print(f"  * ESG Score: {firm['ESG_Score']}/100")
    print(f"  * Baseline Cost of Capital: {firm['Base_Cost_of_Capital']*100:.2f}%")
    print(f"  * Adjusted Cost of Capital: {firm['Actual_Cost_of_Capital']*100:.2f}%")
    print(f"  * Implied Price Pressure (Valuation Distortion): +{firm['Valuation_Distortion_Pct']:.2f}%")


# STEP 4: RISK-ADJUSTED PERFORMANCE ANALYSIS

print("SYSTEMIC PORTFOLIO RISK ANALYSIS")

# Let's see how much "artificial premium" is baked into the Big Four sector as a whole
total_distortion = sum(f["Valuation_Distortion_Pct"] for f in big_four)
avg_sector_distortion = total_distortion / len(big_four)

print(f"Average ESG-Driven Valuation Distortion across the Big 4: {avg_sector_distortion:.2f}%")
if avg_sector_distortion > 5.0:
    print("Risk Assessment: HIGH. The sector shows significant asset pricing distortions driven by ESG mandate pressures.")
else:
    print("Risk Assessment: LOW. Price pressure from sustainable mandates is within safe fundamental limits.")
