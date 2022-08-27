_tp=0

All_Ids=[43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58]
All_Daxes=[


'''// DAX Query 43
DEFINE
//var _tp=@taxPeriodKey
  VAR __DS0FilterTable = 
    FILTER(
      KEEPFILTERS(VALUES('B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id])),
      NOT(ISBLANK('B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id]))
    )

  //VAR __DS0FilterTable2 =  TREATAS({_tp}, 'B_Dim_Date_Decs'[Year_Quarter_Period])

  VAR __DS0FilterTable3 = 
    TREATAS({"صفري"}, 'B_Dim_DeclarationTypes'[Name])

  VAR __DS0FilterTable4 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[SalesVat])),
      'C_Dim_Declarations'[SalesVat] = 0
    )

  VAR __DS0FilterTable5 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[PurchaseVat])),
      'C_Dim_Declarations'[PurchaseVat] = 0
    )

  VAR __DS0FilterTable6 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[SalesTotal])),
      'C_Dim_Declarations'[SalesTotal] = 0
    )

  VAR __DS0FilterTable7 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[PurchaseTotal])),
      'C_Dim_Declarations'[PurchaseTotal] = 0
    )

  VAR __DS0FilterTable8 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[RecivableTax])),
      'C_Dim_Declarations'[RecivableTax] = 0
    )

  VAR __DS0FilterTable9 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[TotalTaxValue])),
      'C_Dim_Declarations'[TotalTaxValue] = 0
    )

  VAR __DS0FilterTable10 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[TableTaxTotal])),
      'C_Dim_Declarations'[TableTaxTotal] = 0
    )

  VAR __DS0FilterTable11 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[TableTaxVat])),
      'C_Dim_Declarations'[TableTaxVat] = 0
    )

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          A_Dim_Districts_Vat[DistrictVat_Code],
          'B_Dim_Date_Decs'[Year_Quarter_Period],
          'B_Dim_Registered_TaxPayers_A'[Activity_Level_2_Description],
          __DS0FilterTable,
         // __DS0FilterTable2,
          __DS0FilterTable3,
          __DS0FilterTable4,
          __DS0FilterTable5,
          __DS0FilterTable6,
          __DS0FilterTable7,
          __DS0FilterTable8,
          __DS0FilterTable9,
          __DS0FilterTable10,
          __DS0FilterTable11,
          "TAX_LOSS", 'D_Dim_Gamarek_Invoices_Master'[TAX_LOSS]
        )
      ),
      [TAX_LOSS] <> 0
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(
     
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
            A_Dim_Districts_Vat[DistrictVat_Code],
          'B_Dim_Date_Decs'[Year_Quarter_Period],
          'B_Dim_Registered_TaxPayers_A'[Activity_Level_2_Description]
      ,
      __DS0FilterTable,
      //__DS0FilterTable2,
      __DS0FilterTable3,
      __DS0FilterTable4,
      __DS0FilterTable5,
      __DS0FilterTable6,
      __DS0FilterTable7,
      __DS0FilterTable8,
      __DS0FilterTable9,
      __DS0FilterTable10,
      __DS0FilterTable11,
      __ValueFilterDM1,
      "TAX_LOSS", 'D_Dim_Gamarek_Invoices_Master'[TAX_LOSS]
    )

EVALUATE
 SELECTCOLUMNS ( __DS0Core ,
 
    "UniqueTaxId", 'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name", 'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address", 'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "Period", 'B_Dim_Date_Decs'[Year_Quarter_Period],
    "TaxLoss",IF(ISBLANK([TAX_LOSS]),0, IF([TAX_LOSS]<0, [TAX_LOSS]*(-1), [TAX_LOSS])),
    
    "Activity",   "غير معلوم",
    "ActivityL2", "غير معلوم",
    "District",    A_Dim_Districts_Vat[DistrictVat_Code],
    "RegionId",0,
    "PurchaseInOtherSalesTax",  0,
    "SalesInOtherPurchasesTax", 0,
    "DeclarationID",0 , 
	"Dim_Declarations'[Dec_ID_S]", 0,
    "SalesInOtherPurchases", 0,
    "PurchasesInOtherSales", 0,
    "SalesInvoicesCountInOthers",   0,
    "PurchaseInvoiceCountInOthers", 0,
    "TaxPayerID",0,
    "DeclaredSalesTax", 0
    
    
    )

'''

,


'''// DAX Query 44
DEFINE
//var _tp=@taxPeriodKey
  VAR __DS0FilterTable = 
    FILTER(
      KEEPFILTERS(VALUES('B_Dim_Registered_TaxPayers_A'[is_sent_Zero_or_NoValue_Dec_3times])),
      NOT(
        OR(
          OR(
            ISBLANK('B_Dim_Registered_TaxPayers_A'[is_sent_Zero_or_NoValue_Dec_3times]),
            'B_Dim_Registered_TaxPayers_A'[is_sent_Zero_or_NoValue_Dec_3times] = 0
          ),
          'B_Dim_Registered_TaxPayers_A'[is_sent_Zero_or_NoValue_Dec_3times] = 1
        )
      )
    )

  VAR __DS0FilterTable2 = 
    FILTER(
      KEEPFILTERS(VALUES('B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id])),
      NOT(ISBLANK('B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id]))
    )

  VAR __DS0FilterTable3 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[SalesVatt])),
      'C_Dim_Declarations'[SalesVatt] = 0
    )

  VAR __DS0FilterTable4 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[PurchaseVat])),
      'C_Dim_Declarations'[PurchaseVat] = 0
    )

  //VAR __DS0FilterTable5 =  TREATAS({_tp}, 'B_Dim_Date_Decs'[taxperiod])

  VAR __DS0FilterTable6 = 
    TREATAS({"صفري"}, 'B_Dim_DeclarationTypes'[Name])

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(
     
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'B_Dim_Date_Decs'[taxperiod],
          'B_Dim_Registered_TaxPayers_A'[Activity_Level_1_Description],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
           A_Dim_Region[RegionCode],

      __DS0FilterTable,
      __DS0FilterTable2,
      __DS0FilterTable3,
      __DS0FilterTable4,
      //__DS0FilterTable5,
      __DS0FilterTable6,
      "Real_Sales_Product_Total_tax_value",    'D_Dim_Invoices_Real'[Real_Sales_Product_Total_tax_value],
      "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value]
    )



EVALUATE
SELECTCOLUMNS (__DS0Core,

    "UniqueTaxId", 'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name",        'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",     'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "Period",      'B_Dim_Date_Decs'[taxperiod],
    "RegionId",    IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",    IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0, A_Dim_Districts_Vat[DistrictVat_Code]),
    
    "PurchaseInOtherSalesTax",  if(ISBLANK([Real_Purchase_Product_Total_tax_value]),0, [Real_Purchase_Product_Total_tax_value]),
    "SalesInOtherPurchasesTax", IF(ISBLANK([Real_Sales_Product_Total_tax_value]), 0, [Real_Sales_Product_Total_tax_value]),
    "TaxLoss",  IF(ISBLANK([Real_Sales_Product_Total_tax_value]),0, 
                IF ([Real_Sales_Product_Total_tax_value]<0, [Real_Sales_Product_Total_tax_value]*(-1), [Real_Sales_Product_Total_tax_value])),
    
    "Activity",   "غير معلوم",
    "ActivityL2", "غير معلوم",
    "DeclarationID", 0 , 
	"Dim_Declarations'[Dec_ID_S]", 0,
    "TaxPayerID", 0, 
    "PurchasesInOtherSales", 0,
    "SalesInvoicesCountInOthers", 0,
    "PurchaseInvoiceCountInOthers", 0,
    "SalesInOtherPurchases", 0,
    "DeclaredSalesTax", 0

    
//    "PurchaseInOtherSalesTax", if(ISBLANK('Dim_Declarations'[Real_Purchases_taxValues]),0,'Dim_Declarations'[Real_Purchases_taxValues]),
//    "SalesInOtherPurchasesTax", 'Dim_Declarations'[Real_Sales_taxValues],
//    "PurchasesInOtherSales", if(ISBLANK('Dim_Declarations'[PurchasesInOtherSales]),0,'Dim_Declarations'[PurchasesInOtherSales]),
//    "SalesInvoicesCountInOthers", 'Dim_Declarations'[SalesInvoicesCountInOthers],
//    "PurchaseInvoiceCountInOthers", if(ISBLANK('Dim_Declarations'[PurchaseInvoiceCountInOthers]),0,'Dim_Declarations'[PurchaseInvoiceCountInOthers]),
//    "SalesInOtherPurchases", 'Dim_Declarations'[SalesInOtherPurchases],
//    "DeclaredSalesTax", 'Dim_Declarations'[SalesVat],
//    "TaxLoss", 'Dim_Declarations'[Real_Sales_taxValues],
    

)



'''
,



'''// DAX Query 45
DEFINE
//var _tp=@taxPeriodKey
  VAR __DS0FilterTable = 
    TREATAS(
      {0,
        1,
        BLANK()},
      'B_Dim_Registered_TaxPayers_A'[is_sent_Zero_or_NoValue_Dec_3times]
    )

  VAR __DS0FilterTable2 = 
    FILTER(
      KEEPFILTERS(VALUES('B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id])),
      NOT(ISBLANK('B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id]))
    )

  VAR __DS0FilterTable3 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[PurchaseVat])),
      'C_Dim_Declarations'[PurchaseVat] = 0
    )

  VAR __DS0FilterTable4 = 
    FILTER(
      KEEPFILTERS(VALUES('C_Dim_Declarations'[SalesVatt])),
      'C_Dim_Declarations'[SalesVatt] = 0
    )

  //VAR __DS0FilterTable5 = TREATAS({_tp}, 'B_Dim_Date_Decs'[taxperiod])

  VAR __DS0FilterTable6 = 
    TREATAS({"صفري"}, 'B_Dim_DeclarationTypes'[Name])

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(
      
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'B_Dim_Date_Decs'[taxperiod],
          'B_Dim_Registered_TaxPayers_A'[Activity_Level_1_Description],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
           A_Dim_Region[RegionCode]
       ,
      __DS0FilterTable,
      __DS0FilterTable2,
      __DS0FilterTable3,
      __DS0FilterTable4,
     // __DS0FilterTable5,
      __DS0FilterTable6,
      "Real_Sales_Product_Total_tax_value",    'D_Dim_Invoices_Real'[Real_Sales_Product_Total_tax_value],
      "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value]
    )

  

EVALUATE
SELECTCOLUMNS ( __DS0Core,

    "UniqueTaxId", 'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name",        'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",     'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "Period",      'B_Dim_Date_Decs'[taxperiod],
    "RegionId",    IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",    IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0, A_Dim_Districts_Vat[DistrictVat_Code]),
    
    
    "PurchaseInOtherSalesTax",  if(ISBLANK('D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value]),0,[Real_Purchase_Product_Total_tax_value]),
    "SalesInOtherPurchasesTax", if(ISBLANK([Real_Sales_Product_Total_tax_value]),0, [Real_Sales_Product_Total_tax_value]),
    "TaxLoss",  IF(ISBLANK([Real_Sales_Product_Total_tax_value]),0, 
                IF ([Real_Sales_Product_Total_tax_value]<0, [Real_Sales_Product_Total_tax_value]*(-1), [Real_Sales_Product_Total_tax_value])),

    "Activity",   "غير معلوم",
    "ActivityL2", "غير معلوم", 
    "DeclarationID", 0, 
	"'Dim_Declarations'[Dec_ID_S]", 0,
    "TaxPayerID","",
    "SalesInOtherPurchases", 0,
    "PurchasesInOtherSales", 0,
    "SalesInvoicesCountInOthers", 0, 
    "PurchaseInvoiceCountInOthers", 0,
    "DeclaredSalesTax",  0
    
//    "PurchaseInOtherSalesTax", if(ISBLANK('Dim_Declarations'[Real_Purchases_taxValues]),0,'Dim_Declarations'[Real_Purchases_taxValues]),
//    "SalesInOtherPurchasesTax", 'Dim_Declarations'[Real_Sales_taxValues],
//    "SalesInOtherPurchases", 'Dim_Declarations'[SalesInOtherPurchases],
//    "PurchasesInOtherSales", if(ISBLANK('Dim_Declarations'[PurchasesInOtherSales]),0,'Dim_Declarations'[PurchasesInOtherSales]),
//    "SalesInvoicesCountInOthers", 'Dim_Declarations'[SalesInvoicesCountInOthers],
//    "PurchaseInvoiceCountInOthers", if(ISBLANK('Dim_Declarations'[PurchaseInvoiceCountInOthers]),0,'Dim_Declarations'[PurchaseInvoiceCountInOthers]),
//    "TaxLoss", 'Dim_Declarations'[Real_Sales_taxValues], 
//    "DeclaredSalesTax", 'Dim_Declarations'[SalesVat]

    
)

'''
,

'''// DAX Query 46
DEFINE
//var _tp=@taxPeriodKey
  //VAR __DS0FilterTable = TREATAS({_tp}, 'B_Dim_Date_Decs'[taxperiod])

  VAR __DS0FilterTable2 = 
    TREATAS({BLANK()}, 'B_Dim_Registered_TaxPayers_A'[is_Dummy_Company])

  VAR __DS0FilterTable3 = 
    TREATAS({TRUE}, 'B_Dim_TaxPayers_Universe_B'[IS_Dummy])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
          'B_Dim_Date_Decs'[taxperiod],
          //__DS0FilterTable,
          __DS0FilterTable2,
          __DS0FilterTable3,
          "DEC_Sum_Sales_VAT",    'C_Dim_Declarations'[DEC_Sum_Sales_VAT],
          "DEC_Sum_Purchase_VAT", 'C_Dim_Declarations'[DEC_Sum_Purchase_VAT],
          "est5las_Purchase_Flag", IGNORE('C_Dim_Declarations'[est5las_Purchase_Flag]),
          "est5las_Sales_Flag",    IGNORE('C_Dim_Declarations'[est5las_Sales_Flag])
        )
      ),
      AND([est5las_Purchase_Flag] = 0, [est5las_Sales_Flag] = 0)
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(
      
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
          'B_Dim_Date_Decs'[taxperiod]
    ,
      //__DS0FilterTable,
      __DS0FilterTable2,
      __DS0FilterTable3,
      __ValueFilterDM1,
      "DEC_Sum_Sales_VAT", 'C_Dim_Declarations'[DEC_Sum_Sales_VAT],
      "DEC_Sum_Purchase_VAT", 'C_Dim_Declarations'[DEC_Sum_Purchase_VAT]
    )

  
EVALUATE
SELECTCOLUMNS ( __DS0Core ,
 
    "UniqueTaxId",      'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name",             'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "Period",           'B_Dim_Date_Decs'[taxperiod],
    "RegionId",             IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",             IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0, A_Dim_Districts_Vat[DistrictVat_Code]),    
    "DEC_Sum_Sales_VAT",    IF(ISBLANK([DEC_Sum_Sales_VAT]),0, IF([DEC_Sum_Sales_VAT]<0, [DEC_Sum_Sales_VAT]*(-1), [DEC_Sum_Sales_VAT])) ,
    "DEC_Sum_Purchase_VAT", IF(ISBLANK([DEC_Sum_Purchase_VAT]),0, IF([DEC_Sum_Purchase_VAT]<0, [DEC_Sum_Purchase_VAT]*(-1), [DEC_Sum_Purchase_VAT])), 
    "TaxLoss",              IF(ISBLANK([DEC_Sum_Purchase_VAT]),0, IF([DEC_Sum_Purchase_VAT]<0, [DEC_Sum_Purchase_VAT]*(-1), [DEC_Sum_Purchase_VAT])), 

    
    //"TaxLoss",'Dim_Declarations'[Purchases_Vat_With_Dummy],
    
    "DeclarationID", 0,
    "TaxPayerID", 0,
    "PurchaseInvoiceCountInOthers", 0,
    "PurchasesInOtherSales", 0,
    "PurchaseInOtherSalesTax", 0,
    "SalesInOtherPurchasesTax", 0,
    "SalesInOtherPurchases", 0,
    "SalesInvoicesCountInOthers", 0,
    "Activity", "غير معلوم",
    "ActivityL2", "غير معلوم",
    "DeclaredSalesTax", 0

)


'''

,

'''// DAX Query 47
DEFINE
 // var _tp=@taxPeriodKey
  
 VAR __DS0FilterTable =   TREATAS({TRUE}, 'B_Dim_TaxPayers_Universe_Master'[IS_Not_Registered])

  VAR __DS0FilterTable2 = 
    TREATAS(
      {"إتفاقيات",
        "جدول",
        "قيمة مضافة",
        BLANK()},
      'B_Dim_DeclarationTypes'[Name]
    )


 // VAR __DS0FilterTable3 =  TREATAS({_tp}, 'B_Dim_Date_Invs'[taxperiod])

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(

          'B_Dim_Date_Invs'[taxperiod],
          'B_Dim_TaxPayers_Universe_Master'[Taxpayer_Name],
          'B_Dim_TaxPayers_Universe_Master'[Unique_Tax_Id],
          'B_Dim_TaxPayers_Universe_Master'[Region_Code],
          'B_Dim_TaxPayers_Universe_Master'[DistrictVat_Code]
,
      __DS0FilterTable,
      __DS0FilterTable2,
     // __DS0FilterTable3,
      
      "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
      "Real_Sales_Product_Total_tax_value",    'D_Dim_Invoices_Real'[Real_Sales_Product_Total_tax_value]
    )

 
EVALUATE 
 SELECTCOLUMNS ( __DS0Core ,
 
    "Period",        LEFT('B_Dim_Date_Invs'[taxperiod], 6 ), // Comment Left ...
    "UniqueTaxId",   'B_Dim_TaxPayers_Universe_Master'[Unique_Tax_Id],
    "Name",          'B_Dim_TaxPayers_Universe_Master'[Taxpayer_Name],
    "Address", "",
    "RegionId",    IF(ISBLANK('B_Dim_TaxPayers_Universe_Master'[Region_Code]), 0, 'B_Dim_TaxPayers_Universe_Master'[Region_Code]),
    "District",    IF(ISBLANK('B_Dim_TaxPayers_Universe_Master'[DistrictVat_Code]), 0, 'B_Dim_TaxPayers_Universe_Master'[DistrictVat_Code]),
    "District_Vat_Name", 'B_Dim_TaxPayers_Universe_Master'[DistrictVat_Code],
    "Region_Name", 'B_Dim_TaxPayers_Universe_Master'[Region_Code],

    "PurchaseInOtherSalesTax",      IF(ISBLANK([Real_Purchase_Product_Total_tax_value]), 0, [Real_Purchase_Product_Total_tax_value]),
    "SalesInOtherPurchasesTax",     IF(ISBLANK([Real_Sales_Product_Total_tax_value]), 0, [Real_Sales_Product_Total_tax_value]),
    "TaxLoss",  IF(ISBLANK([Real_Sales_Product_Total_tax_value]),0, 
                IF ([Real_Sales_Product_Total_tax_value]<0, [Real_Sales_Product_Total_tax_value]*(-1), [Real_Sales_Product_Total_tax_value])),
    
    "Activity",   "غير معلوم",
    "ActivityL2", "غير معلوم",
    "PurchaseInvoiceCountInOthers", 0,
    "SalesInvoicesCountInOthers",   0,
    "PurchasesInOtherSales",        0,
    "SalesInOtherPurchases",        0,
    "DeclarationID", "",
    "DeclaredSalesTax", "",
    "TaxPayerID", ""

 )
 
 
 '''
,

'''// DAX Query 48
DEFINE
  //var _tp=@taxPeriodKey 
  
  VAR __DS0FilterTable = 
    FILTER(
      KEEPFILTERS(VALUES('B_Dim_Not_Registered_TaxPayers'[rin])),
      NOT(ISBLANK('B_Dim_Not_Registered_TaxPayers'[rin]))
    )

  VAR __DS0FilterTable2 = 
    FILTER(
      KEEPFILTERS(VALUES('B_Dim_Not_Registered_TaxPayers'[regname])),
      NOT(
        AND(
          'B_Dim_Not_Registered_TaxPayers'[regname] = "",
          ISBLANK('B_Dim_Not_Registered_TaxPayers'[regname]) = ISBLANK("")
        )
      )
    )

//  VAR __DS0FilterTable3 = 
//    FILTER(
//      KEEPFILTERS(VALUES('B_Dim_Date_Gamarek'[Year_Quarter_Period])),
//      AND(
//        NOT(ISBLANK('B_Dim_Date_Gamarek'[Year_Quarter_Period])),
//        SEARCH(_tp, 'B_Dim_Date_Gamarek'[Year_Quarter_Period], 1, 0) >= 1
//      )
//    )
    
    
  VAR __DS0Core = 
    SUMMARIZECOLUMNS(

          'B_Dim_Not_Registered_TaxPayers'[rin],
          'B_Dim_Not_Registered_TaxPayers'[regname],
          'D_Dim_Gamarek_Invoices_Master'[CDLRAddress],
          'B_Dim_Date_Gamarek'[Year_Quarter_Period],
          'B_Dim_Not_Registered_TaxPayers'[DistrictVat_Code],
          
      __DS0FilterTable,
      __DS0FilterTable2,
     // __DS0FilterTable3,
      "TAX_LOSS", 'D_Dim_Gamarek_Invoices_Master'[TAX_LOSS]
    )

 
EVALUATE
SELECTCOLUMNS ( __DS0Core,
    
    "UniqueTaxId", 'B_Dim_Not_Registered_TaxPayers'[rin],
    "Name",        'B_Dim_Not_Registered_TaxPayers'[regname],
    "Address",     'D_Dim_Gamarek_Invoices_Master'[CDLRAddress],   
    //"CCPXName",    'D_Dim_Gamarek_Invoices_Master'[CCPXName], //
    "Period",       LEFT('B_Dim_Date_Gamarek'[Year_Quarter_Period],6), //
    
    "TaxLoss", IF(ISBLANK([TAX_LOSS]),0, IF([TAX_LOSS]<0, [TAX_LOSS]*(-1), [TAX_LOSS])),

    "District", 'B_Dim_Not_Registered_TaxPayers'[DistrictVat_Code],
    "RegionId", 0, 
    "Activity", "غير معلوم",
    "ActivityL2", "غير معلوم",
    "PurchaseInOtherSalesTax", 0,
    "SalesInOtherPurchasesTax", 0,
    "DeclarationID","" , 
	"Dim_Declarations'[Dec_ID_S]", "",
    "SalesInOtherPurchases", 0,
    "PurchasesInOtherSales", 0,
    "SalesInvoicesCountInOthers", 0,
    "PurchaseInvoiceCountInOthers", 0,
    "TaxPayerID","",
    "DeclaredSalesTax", ""
    
    )    
    '''
    ,

    '''// DAX Query 49
DEFINE
//var _tp=@taxPeriodKey
  VAR __DS0FilterTable = 
    TREATAS({TRUE}, 'B_Dim_Registered_TaxPayers_A'[is_Dummy_Company])

  VAR __DS0FilterTable2 = 
    FILTER(
      KEEPFILTERS(VALUES('B_Dim_DeclarationTypes'[Name])),
      NOT('B_Dim_DeclarationTypes'[Name] = "صفري")
    )

  //VAR __DS0FilterTable3 =   TREATAS({_tp}, 'B_Dim_Date_Decs'[taxperiod])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
          'B_Dim_Date_Decs'[taxperiod],
          __DS0FilterTable,
          __DS0FilterTable2,
         // __DS0FilterTable3,
          "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
          "DEC_Sum_Purchase_VAT",                  'C_Dim_Declarations'[DEC_Sum_Purchase_VAT],
          "Diffrent_Purchases_Frauds",             'C_Dim_Declarations'[Diffrent_Purchases_Frauds],
          "est5las_Purchase_Flag", IGNORE('C_Dim_Declarations'[est5las_Purchase_Flag])
        )
      ),
      AND(
        AND([est5las_Purchase_Flag] = 0, [DEC_Sum_Purchase_VAT] <> 0),
        NOT(ISBLANK([DEC_Sum_Purchase_VAT]))
      )
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(
     
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
          'B_Dim_Date_Decs'[taxperiod]
     ,
      __DS0FilterTable,
      __DS0FilterTable2,
      //__DS0FilterTable3,
      __ValueFilterDM1,
      "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
      "DEC_Sum_Purchase_VAT",                  'C_Dim_Declarations'[DEC_Sum_Purchase_VAT],
      "Diffrent_Purchases_Frauds",             'C_Dim_Declarations'[Diffrent_Purchases_Frauds]
    )



EVALUATE
SELECTCOLUMNS ( __DS0Core,

    "UniqueTaxId",      'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],  
    "Name",             'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "Period",           'B_Dim_Date_Decs'[taxperiod], 
    "RegionId",    IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",    IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0, A_Dim_Districts_Vat[DistrictVat_Code]),

    
    "Real_Purchase_Product_Total_tax_value", IF(ISBLANK([Real_Purchase_Product_Total_tax_value]), 0, [Real_Purchase_Product_Total_tax_value]),
    "SumPurchaseVat",                        IF(ISBLANK([DEC_Sum_Purchase_VAT]),0,[DEC_Sum_Purchase_VAT]),
    
    "Diffrent_Purchases_Frauds",             IF(ISBLANK([Diffrent_Purchases_Frauds]),0, 
                                             IF([Diffrent_Purchases_Frauds]<0, [Diffrent_Purchases_Frauds]*(-1), [Diffrent_Purchases_Frauds])),
                                             
    "TaxLoss",                               IF(ISBLANK([Diffrent_Purchases_Frauds]),0, 
                                             IF([Diffrent_Purchases_Frauds]<0, [Diffrent_Purchases_Frauds]*(-1), [Diffrent_Purchases_Frauds])), 
 
    "Activity", "غير معلوم",
    "ActivityL2", "غير معلوم",                                            
    "DeclarationID", 0,
    "SalesInOtherPurchasesTax", 0,
    "SalesInOtherPurchases", 0,
    "SalesInvoicesCountInOthers", 0,
    "DeclaredSalesTax", 0,
    "TaxPayerID", 0
    
    
    //"TaxLoss",     'Dim_Declarations'[Different_Purchases_Case],
    //"PurchaseInOtherSalesTax", [Real_Purchase_Product_Total_tax_value],
    //"PurchaseInvoiceCountInOthers", 'Dim_Declarations'[PurchaseInvoiceCountInOthers],
    //"PurchasesInOtherSales", 'Dim_Declarations'[PurchasesInOtherSales],

    
    )

'''
,

'''// DAX Query 50
DEFINE
  //var _tp=@taxPeriodKey
  
  VAR __DS0FilterTable = 
    FILTER(
      KEEPFILTERS(VALUES('B_Registered_AND_Not_Sending_Decs_Gamarek'[Unique_Tax_Id])),
      NOT(ISBLANK('B_Registered_AND_Not_Sending_Decs_Gamarek'[Unique_Tax_Id]))
    )

//  VAR __DS0FilterTable2 = 
//    FILTER(
//      KEEPFILTERS(VALUES('B_Dim_Date_Gamarek'[Year_Quarter_Period])),
//      AND(
//        AND(
//          NOT(ISBLANK('B_Dim_Date_Gamarek'[Year_Quarter_Period])),
//          SEARCH("2020", 'B_Dim_Date_Gamarek'[Year_Quarter_Period], 1, 0) >= 1
//        ),
//        'B_Dim_Date_Gamarek'[Year_Quarter_Period] IN {_tp}
//      )
//    )

  VAR __DS0FilterTable3 = 
    FILTER(
      KEEPFILTERS(VALUES('A_Gamarek_Districts_Vat'[DistrictVat_Name])),
      NOT(ISBLANK('A_Gamarek_Districts_Vat'[DistrictVat_Name]))
    )

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Registered_AND_Not_Sending_Decs_Gamarek'[Unique_Tax_Id],
          'B_Registered_AND_Not_Sending_Decs_Gamarek'[Taxpayer_Name],
          'B_Registered_AND_Not_Sending_Decs_Gamarek'[Taxpayer_Address],
          'B_Dim_Date_Gamarek'[Year_Quarter_Period],
          'A_Gamarek_Region'[RegionName],
          'A_Gamarek_Districts_Vat'[DistrictVat_Name],
          __DS0FilterTable,
          //__DS0FilterTable2,
          __DS0FilterTable3,
          "TAX_LOSS", 'D_Dim_Gamarek_Invoices_Master'[TAX_LOSS]
        )
      ),
      AND(NOT(ISBLANK([TAX_LOSS])), [TAX_LOSS] <> 0)
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(

          'B_Registered_AND_Not_Sending_Decs_Gamarek'[Unique_Tax_Id],
          'B_Registered_AND_Not_Sending_Decs_Gamarek'[Taxpayer_Name],
          'B_Registered_AND_Not_Sending_Decs_Gamarek'[Taxpayer_Address],
          'B_Dim_Date_Gamarek'[Year_Quarter_Period],
          'A_Gamarek_Region'[RegionName],
          'A_Gamarek_Districts_Vat'[DistrictVat_Name],
          'B_Registered_AND_Not_Sending_Decs_Gamarek'[FK_Region_id],
          'B_Registered_AND_Not_Sending_Decs_Gamarek'[DistrictVAT],

      __DS0FilterTable,
     // __DS0FilterTable2,
      __DS0FilterTable3,
      __ValueFilterDM1,
      
      "TAX_LOSS", 'D_Dim_Gamarek_Invoices_Master'[TAX_LOSS]
    )
    
    
EVALUATE
SELECTCOLUMNS ( __DS0Core,

    "UniqueTaxId",      'B_Registered_AND_Not_Sending_Decs_Gamarek'[Unique_Tax_Id],
    "Name",             'B_Registered_AND_Not_Sending_Decs_Gamarek'[Taxpayer_Name],
    "Address",          'B_Registered_AND_Not_Sending_Decs_Gamarek'[Taxpayer_Address],
    "Period",            LEFT('B_Dim_Date_Gamarek'[Year_Quarter_Period],6),
    "RegionId",          IF(ISBLANK('B_Registered_AND_Not_Sending_Decs_Gamarek'[FK_Region_id]), 0, 'B_Registered_AND_Not_Sending_Decs_Gamarek'[FK_Region_id]),
    "District",          IF(ISBLANK('B_Registered_AND_Not_Sending_Decs_Gamarek'[DistrictVAT]), 0, 'B_Registered_AND_Not_Sending_Decs_Gamarek'[DistrictVAT]),
    "RegionName",       'A_Gamarek_Region'[RegionName],
    "DistrictVat_Name", 'A_Gamarek_Districts_Vat'[DistrictVat_Name],
    
    "TaxLoss",          IF(ISBLANK([TAX_LOSS]),0, IF([TAX_LOSS]<0, [TAX_LOSS]*(-1), [TAX_LOSS])),
    
    "Activity", "غير معلوم",   
    "ActivityL2", "غير معلوم",    
    "PurchaseInOtherSalesTax", 0,
    "SalesInOtherPurchasesTax", 0,
    "DeclarationID","" , 
	"'Dim_Declarations'[Dec_ID_S]", "",
    "SalesInOtherPurchases", 0,
    "PurchasesInOtherSales", 0,
    "SalesInvoicesCountInOthers", 0,
    "PurchaseInvoiceCountInOthers", 0,
    "TaxPayerID","",
    "DeclaredSalesTax", ""
)
 

  
    

 
'''

,


'''// DAX Query 51
DEFINE
 //var _tp=@taxPeriodKey
  VAR __DS0FilterTable = 
    FILTER(
      KEEPFILTERS(VALUES('A_Dim_Distrcts_Vat_not_Sending_Decs'[DistrictVat_Name])),
      NOT(ISBLANK('A_Dim_Distrcts_Vat_not_Sending_Decs'[DistrictVat_Name]))
    )

 // VAR __DS0FilterTable2 =  TREATAS({_tp}, 'B_Dim_Date_Invs'[taxperiod])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Date_Invs'[taxperiod],
          'B_Registered_And_Not_Sending_Decs_A'[Unique_Tax_Id],
          'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Name],
          'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Address],
          'A_Dim_Distrcts_Vat_not_Sending_Decs'[DistrictVat_Code],
        //   A_Dim_Region[RegionCode],
          __DS0FilterTable,
         // __DS0FilterTable2,
          
          "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
          "Real_Sales_Product_Total_tax_value",    'D_Dim_Invoices_Real'[Real_Sales_Product_Total_tax_value],
          "Registered___not_Sending_VAT_Value",    'C_Dim_Payments'[Registered_&_not_Sending_VAT_Value],
          "Registered___not_Sending_Table_Value",  'C_Dim_Payments'[Registered_&_not_Sending_Table_Value]
        )
      ),
      AND(
        OR(
          [Registered___not_Sending_Table_Value] <> 0,
          NOT(ISBLANK([Registered___not_Sending_Table_Value]))
        ),
        OR(
          [Registered___not_Sending_VAT_Value] <> 0,
          NOT(ISBLANK([Registered___not_Sending_VAT_Value]))
        )
      )
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(
      
          'B_Dim_Date_Invs'[taxperiod],
          'B_Registered_And_Not_Sending_Decs_A'[Unique_Tax_Id],
          'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Name],
          'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Address],
          'A_Dim_Distrcts_Vat_not_Sending_Decs'[DistrictVat_Code],
          // A_Dim_Region[RegionCode],
           
      __DS0FilterTable,
      //__DS0FilterTable2,
      __ValueFilterDM1,
      
      "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
      "Real_Sales_Product_Total_tax_value",    'D_Dim_Invoices_Real'[Real_Sales_Product_Total_tax_value],
      "Registered___not_Sending_VAT_Value",    'C_Dim_Payments'[Registered_&_not_Sending_VAT_Value],
      "Registered___not_Sending_Table_Value",  'C_Dim_Payments'[Registered_&_not_Sending_Table_Value]
    )

EVALUATE
SELECTCOLUMNS (  __DS0Core,

    "UniqueTaxId",       'B_Registered_And_Not_Sending_Decs_A'[Unique_Tax_Id],
    "Name",              'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Name],
    "Address",           'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Address],
    "Period",            LEFT ( 'B_Dim_Date_Invs'[taxperiod], 6 ),
    "RegionId",    0,//IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",    IF(ISBLANK(A_Dim_Distrcts_Vat_not_Sending_Decs[DistrictVat_Code]), 0, A_Dim_Distrcts_Vat_not_Sending_Decs[DistrictVat_Code]),

    
    "SalesInvoicesCountInOthers",  IF(ISBLANK([Real_Sales_Total_Money]),0, IF([Real_Sales_Total_Money]<0, [Real_Sales_Total_Money]*(-1), [Real_Sales_Total_Money])),
    
    
    "PurchaseInvoiceCountInOthers", IF(ISBLANK([Real_Purchase_Total_Money]),0, IF([Real_Purchase_Total_Money]<0, [Real_Purchase_Total_Money]*(-1), [Real_Purchase_Total_Money])),
    
	"PurchaseInOtherSalesTax",      IF(ISBLANK([Real_Purchase_Product_Total_tax_value]),0, 
                                    IF([Real_Purchase_Product_Total_tax_value]<0, [Real_Purchase_Product_Total_tax_value]*(-1), [Real_Purchase_Product_Total_tax_value])),                 
	
    "SalesInOtherPurchasesTax",     IF(ISBLANK([Real_Sales_Product_Total_tax_value]),0, 
                                    IF([Real_Sales_Product_Total_tax_value]<0, [Real_Sales_Product_Total_tax_value]*(-1), [Real_Sales_Product_Total_tax_value])), 
    
    "TaxLoss",                      IF(ISBLANK([Real_Sales_Product_Total_tax_value]),0, 
                                    IF([Real_Sales_Product_Total_tax_value]<0, [Real_Sales_Product_Total_tax_value]*(-1), [Real_Sales_Product_Total_tax_value])),
    
    "PurchasesInOtherSales", 0,
    "SalesInOtherPurchases", 0,
    "Activity", "غير معلوم",
    "ActivityL2", "غير معلوم",
    "TaxPayerID", 0,
    "DeclarationID", "",
    "DeclaredSalesTax", "" 

    
    
//    "PurchaseInvoiceCountInOthers", 'get_taxpayers_notsending_dec'[count_purchases_in_others],
//    "SalesInvoicesCountInOthers",   'get_taxpayers_notsending_dec'[count_sales_in_others],
//    "SalesInOtherPurchases",        'get_taxpayers_notsending_dec'[SalesInOtherPurchases],
//    "SalesInOtherPurchasesTax",     'get_taxpayers_notsending_dec'[Real_Sales_taxValues],
//    "PurchasesInOtherSales",        'get_taxpayers_notsending_dec'[PurchasesInOtherSales],
//    "PurchaseInOtherSalesTax",      'get_taxpayers_notsending_dec'[Real_Purchases_taxValues],
//    "TaxLoss",                      'get_taxpayers_notsending_dec'[Real_Sales_taxValues],
    

)




'''
,


'''// DAX Query 52
DEFINE
  //var _tp=@taxPeriodKey  
  
  VAR __DS0FilterTable = 
    FILTER(
      KEEPFILTERS(VALUES('A_Dim_Distrcts_Vat_not_Sending_Decs'[DistrictVat_Name])),
      NOT(ISBLANK('A_Dim_Distrcts_Vat_not_Sending_Decs'[DistrictVat_Name]))
    )
  
  // VAR __DS0FilterTable2 = TREATAS({_tp}, 'B_Dim_Date_Invs'[taxperiod])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Date_Invs'[taxperiod],
          'B_Registered_And_Not_Sending_Decs_A'[Unique_Tax_Id],
          'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Name],
          'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Address],
          'A_Dim_Distrcts_Vat_not_Sending_Decs'[DistrictVat_Code],
          __DS0FilterTable,
         // __DS0FilterTable2,
          "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
          "Real_Sales_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Sales_Product_Total_tax_value],
          "Registered___not_Sending_Table_Value", IGNORE('C_Dim_Payments'[Registered_&_not_Sending_Table_Value]),
          "Registered___not_Sending_VAT_Value", IGNORE('C_Dim_Payments'[Registered_&_not_Sending_VAT_Value])
        )
      ),
      AND(
        AND(
          [Registered___not_Sending_Table_Value] = 0,
          ISBLANK([Registered___not_Sending_Table_Value])
        ),
        OR(
          ISBLANK([Registered___not_Sending_VAT_Value]),
          [Registered___not_Sending_VAT_Value] = 0
        )
      )
    )
    
    VAR __DS0Core = 
    SUMMARIZECOLUMNS(
     
          'B_Dim_Date_Invs'[taxperiod],
          'B_Registered_And_Not_Sending_Decs_A'[Unique_Tax_Id],
          'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Name],
          'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Address],
          'A_Dim_Distrcts_Vat_not_Sending_Decs'[DistrictVat_Code],
           A_Dim_Region[RegionCode],
           
      __DS0FilterTable,
     // __DS0FilterTable2,
      __ValueFilterDM1,
      "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
      "Real_Sales_Product_Total_tax_value",    'D_Dim_Invoices_Real'[Real_Sales_Product_Total_tax_value],
      "Registered___not_Sending_Table_Value", IGNORE('C_Dim_Payments'[Registered_&_not_Sending_Table_Value]),
      "Registered___not_Sending_VAT_Value", IGNORE('C_Dim_Payments'[Registered_&_not_Sending_VAT_Value])
    )

 
EVALUATE
SELECTCOLUMNS ( __DS0Core,
    
    "UniqueTaxId",        'B_Registered_And_Not_Sending_Decs_A'[Unique_Tax_Id],
    "Name",               'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Name],
    "Address",            'B_Registered_And_Not_Sending_Decs_A'[Taxpayer_Address],
    "Period",              LEFT ( 'B_Dim_Date_Invs'[taxperiod], 6 ),
    "RegionId",    IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",    IF(ISBLANK(A_Dim_Distrcts_Vat_not_Sending_Decs[DistrictVat_Code]), 0, A_Dim_Distrcts_Vat_not_Sending_Decs[DistrictVat_Code]),

    
    "PurchaseInOtherSalesTax",     IF(ISBLANK([Real_Purchase_Product_Total_tax_value]),0, 
                                   IF([Real_Purchase_Product_Total_tax_value]<0, [Real_Purchase_Product_Total_tax_value]*(-1), [Real_Purchase_Product_Total_tax_value])),
    
    "SalesInOtherPurchasesTax",    IF(ISBLANK([Real_Sales_Product_Total_tax_value]),0, 
                                   IF([Real_Sales_Product_Total_tax_value]<0, [Real_Sales_Product_Total_tax_value]*(-1), [Real_Sales_Product_Total_tax_value])),

    "TaxLoss",                     IF(ISBLANK([Real_Sales_Product_Total_tax_value]),0, 
                                   IF([Real_Sales_Product_Total_tax_value]<0, [Real_Sales_Product_Total_tax_value]*(-1), [Real_Sales_Product_Total_tax_value])),

    "PurchaseInvoiceCountInOthers", 0,
    "SalesInvoicesCountInOthers",   0,
    "SalesInOtherPurchases", 0,
    "PurchasesInOtherSales", 0,
    
    "Activity", "غير معلوم", 
    "ActivityL2", "غير معلوم",
    "TaxPayerID", "",
    "DeclarationID", "",
    "DeclaredSalesTax", ""
    
    )





'''
,

'''// DAX Query 53
DEFINE
 // VAR _tp=@taxPeriodKey

  VAR __DS0FilterTable = 
    FILTER(
      KEEPFILTERS(VALUES('B_Dim_DeclarationTypes'[Name])),
      NOT('B_Dim_DeclarationTypes'[Name] = "صفري")
    )

  //VAR __DS0FilterTable2 =  TREATAS({_tp}, 'B_Dim_Date_Decs'[Year_Quarter_Period])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionName],
          'A_Dim_Districts_Vat'[DistrictVat_Name],
          'B_Dim_Date_Decs'[Year_Quarter_Period],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
          
          __DS0FilterTable,
        //  __DS0FilterTable2,
          
          "Diffrent_Sales_Frauds", 'C_Dim_Declarations'[Diffrent_Sales_Frauds],
          "DEC_Sum_Sales_VAT", 'C_Dim_Declarations'[DEC_Sum_Sales_VAT],
          "Real_Sales_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Sales_Product_Total_tax_value],
          "est5las_Sales_Flag", IGNORE('C_Dim_Declarations'[est5las_Sales_Flag])
        )
      ),
      AND(
        AND(
          AND(
            AND(
              AND([est5las_Sales_Flag] = 0, NOT(ISBLANK([Diffrent_Sales_Frauds]))),
              [Diffrent_Sales_Frauds] < -1000
            ),
            NOT(ISBLANK([DEC_Sum_Sales_VAT]))
          ),
          [DEC_Sum_Sales_VAT] <> 0
        ),
        NOT(ISBLANK([Real_Sales_Product_Total_tax_value]))
      )
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(

          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionName],
          'A_Dim_Districts_Vat'[DistrictVat_Name],
          'B_Dim_Date_Decs'[Year_Quarter_Period],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],

      __DS0FilterTable,
    //  __DS0FilterTable2,
      __ValueFilterDM1,
      
      "Diffrent_Sales_Frauds", 'C_Dim_Declarations'[Diffrent_Sales_Frauds],
      "DEC_Sum_Sales_VAT", 'C_Dim_Declarations'[DEC_Sum_Sales_VAT],
      "Real_Sales_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Sales_Product_Total_tax_value]
    )

  
EVALUATE
SELECTCOLUMNS (  __DS0Core ,

    "UniqueTaxId", 'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name",        'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",     'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "Period",      'B_Dim_Date_Decs'[Year_Quarter_Period],   //'Dim_Date'[year_quarter_period]    
    "RegionId",    IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",    IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0, A_Dim_Districts_Vat[DistrictVat_Code]),

    
    "TaxLoss",                  IF(ISBLANK([Diffrent_Sales_Frauds]),0, 
                                IF([Diffrent_Sales_Frauds]<0, [Diffrent_Sales_Frauds]*(-1), [Diffrent_Sales_Frauds])), //[SumSalesVat]-[SumReal_Sales_taxValue]
    
    "SalesInOtherPurchasesTax", IF(ISBLANK([Real_Sales_Product_Total_tax_value]),0, 
                                IF([Real_Sales_Product_Total_tax_value]<0, [Real_Sales_Product_Total_tax_value]*(-1), [Real_Sales_Product_Total_tax_value])), 
    
    "DeclaredSalesTax",         IF(ISBLANK([DEC_Sum_Sales_VAT]),0, IF([DEC_Sum_Sales_VAT]<0, [DEC_Sum_Sales_VAT]*(-1), [DEC_Sum_Sales_VAT])),
    
    "DeclarationID", 0,
    "TaxPayerID", 0,
    "PurchaseInvoiceCountInOthers", 0,
    "PurchasesInOtherSales", 0,
    "PurchaseInOtherSalesTax", 0,
    "SalesInOtherPurchases", 0,
    "SalesInvoicesCountInOthers", 0,
    "Activity",   "غير معلوم",
    "ActivityL2", "غير معلوم"

) 
'''

,
'''// DAX Query 54
DEFINE
  //var _tp=@taxPeriodKey
  //VAR __DS0FilterTable = TREATAS({_tp}, 'B_Dim_Date_Decs'[taxperiod])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Date_Decs'[taxperiod],
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
          
         // __DS0FilterTable,
          
          "Diffrent_Purchases_Frauds",             'C_Dim_Declarations'[Diffrent_Purchases_Frauds],
          "DEC_Sum_Purchase_VAT",                  'C_Dim_Declarations'[DEC_Sum_Purchase_VAT],
          "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
          "Dec_Sum_Purchase_Vat_After_Gamarek",    'C_Dim_Declarations'[Dec_Sum_Purchase_Vat_After_Gamarek],
          "Ezn_Efrag_Purchase_TOTAL",              'D_Dim_Invoices_PORTAL'[Ezn_Efrag_Purchase_TOTAL],
          
          "est5las_Purchase_Flag", IGNORE('C_Dim_Declarations'[est5las_Purchase_Flag])
        )
      ),
      AND(
        AND(
          AND(
            AND(NOT(ISBLANK([DEC_Sum_Purchase_VAT])), [DEC_Sum_Purchase_VAT] <> 0),
            [Diffrent_Purchases_Frauds] < -1000
          ),
          [est5las_Purchase_Flag] = 0
        ),
        NOT(ISBLANK([Real_Purchase_Product_Total_tax_value]))
      )
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(
          'B_Dim_Date_Decs'[taxperiod],
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
      
      //__DS0FilterTable,
      __ValueFilterDM1,
      
      "Diffrent_Purchases_Frauds",             'C_Dim_Declarations'[Diffrent_Purchases_Frauds],
      "DEC_Sum_Purchase_VAT",                  'C_Dim_Declarations'[DEC_Sum_Purchase_VAT],
      "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
      "Dec_Sum_Purchase_Vat_After_Gamarek",    'C_Dim_Declarations'[Dec_Sum_Purchase_Vat_After_Gamarek],
      "Ezn_Efrag_Purchase_TOTAL",              'D_Dim_Invoices_PORTAL'[Ezn_Efrag_Purchase_TOTAL]
    )

EVALUATE

//__DS0Core

SELECTCOLUMNS ( __DS0Core ,
    
    "UniqueTaxId", 'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name",        'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",     'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "RegionId",    IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",    IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0, A_Dim_Districts_Vat[DistrictVat_Code]),

    
    "TaxLoss",                 IF(ISBLANK([Diffrent_Purchases_Frauds]),0, 
                               IF([Diffrent_Purchases_Frauds]<0, [Diffrent_Purchases_Frauds]*(-1), [Diffrent_Purchases_Frauds])),
                               
    "PurchaseInOtherSalesTax", IF(ISBLANK([Real_Purchase_Product_Total_tax_value]),0, 
                               IF([Real_Purchase_Product_Total_tax_value]<0, [Real_Purchase_Product_Total_tax_value]*(-1), [Real_Purchase_Product_Total_tax_value])),
    
    "DeclaredSalesTax",        IF(ISBLANK([DEC_Sum_Purchase_VAT]),0, IF([DEC_Sum_Purchase_VAT]<0, [DEC_Sum_Purchase_VAT]*(-1), [DEC_Sum_Purchase_VAT])), 

    "Period", 'B_Dim_Date_Decs'[taxperiod], 
    "Activity",   "غير معلوم",     
    "ActivityL2", "غير معلوم",
    
    "SalesInOtherPurchasesTax", 0,
    "DeclarationID", 0,
    "Dim_Declarations[Dec_ID_S]", 0,
    "SalesInOtherPurchases", 0,
    "PurchasesInOtherSales", 0,
    "SalesInvoicesCountInOthers", 0,
    "PurchaseInvoiceCountInOthers", 0,
    "TaxPayerID", 0


)




'''

,

'''// DAX Query 55
DEFINE
  // VAR _tp=@taxPeriodKey
  
  VAR __DS0FilterTable = 
    FILTER(
      KEEPFILTERS(VALUES('B_Dim_DeclarationTypes'[Name])),
      NOT('B_Dim_DeclarationTypes'[Name] = "صفري")
    )

  // VAR __DS0FilterTable2 = TREATAS({_tp}, 'C_Dim_Declarations'[TaxPeriod])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionName],
          'A_Dim_Districts_Vat'[DistrictVat_Name],
          'B_Dim_Date_Decs'[taxperiod],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
          
          
          __DS0FilterTable,
         // __DS0FilterTable2,
          
          "Diffrent_Purchases_Frauds", 'C_Dim_Declarations'[Diffrent_Purchases_Frauds],
          "DEC_Sum_Purchase_VAT", 'C_Dim_Declarations'[DEC_Sum_Purchase_VAT],
          "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
          "Dec_Sum_Purchase_Vat_After_Gamarek", 'C_Dim_Declarations'[Dec_Sum_Purchase_Vat_After_Gamarek],
          "Ezn_Efrag_Purchase_TOTAL", 'D_Dim_Invoices_PORTAL'[Ezn_Efrag_Purchase_TOTAL],
          "est5las_Purchase_Flag", IGNORE('C_Dim_Declarations'[est5las_Purchase_Flag])
        )
      ),
      AND(
        AND(
          AND(
            AND(
              AND([est5las_Purchase_Flag] = 0, NOT(ISBLANK([DEC_Sum_Purchase_VAT]))),
              [DEC_Sum_Purchase_VAT] <> 0
            ),
            NOT(ISBLANK([Diffrent_Purchases_Frauds]))
          ),
          [Diffrent_Purchases_Frauds] > 1000
        ),
        NOT(ISBLANK([Real_Purchase_Product_Total_tax_value]))
      )
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(

          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionName],
          'A_Dim_Districts_Vat'[DistrictVat_Name],
          'B_Dim_Date_Decs'[taxperiod],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],

      __DS0FilterTable,
     // __DS0FilterTable2,
      __ValueFilterDM1,
      
      "Diffrent_Purchases_Frauds", 'C_Dim_Declarations'[Diffrent_Purchases_Frauds],
      "DEC_Sum_Purchase_VAT", 'C_Dim_Declarations'[DEC_Sum_Purchase_VAT],
      "Real_Purchase_Product_Total_tax_value", 'D_Dim_Invoices_Real'[Real_Purchase_Product_Total_tax_value],
      "Dec_Sum_Purchase_Vat_After_Gamarek", 'C_Dim_Declarations'[Dec_Sum_Purchase_Vat_After_Gamarek],
      "Ezn_Efrag_Purchase_TOTAL", 'D_Dim_Invoices_PORTAL'[Ezn_Efrag_Purchase_TOTAL]
    )

EVALUATE
SELECTCOLUMNS (  __DS0Core ,
    
    "UniqueTaxId", 'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name",        'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",     'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address], 
    "RegionId",    IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",    IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0, A_Dim_Districts_Vat[DistrictVat_Code]),

    "TaxLoss",                 IF(ISBLANK([Diffrent_Purchases_Frauds]),0, 
                               IF([Diffrent_Purchases_Frauds]<0, [Diffrent_Purchases_Frauds]*(-1), [Diffrent_Purchases_Frauds])),
                               
    "PurchaseInOtherSalesTax", IF(ISBLANK([Real_Purchase_Product_Total_tax_value]),0, 
                               IF([Real_Purchase_Product_Total_tax_value]<0, [Real_Purchase_Product_Total_tax_value]*(-1), [Real_Purchase_Product_Total_tax_value])),
    
    "DeclaredSalesTax",        IF(ISBLANK([DEC_Sum_Purchase_VAT]),0, IF([DEC_Sum_Purchase_VAT]<0, [DEC_Sum_Purchase_VAT]*(-1), [DEC_Sum_Purchase_VAT])), 

    "Dec_Sum_Purchase_Vat_After_Gamarek", IF(ISBLANK([Dec_Sum_Purchase_Vat_After_Gamarek]),0, IF([Dec_Sum_Purchase_Vat_After_Gamarek]<0, [Dec_Sum_Purchase_Vat_After_Gamarek]*(-1), [Dec_Sum_Purchase_Vat_After_Gamarek])), 
    
    
    "Ezn_Efrag_Purchase_TOTAL", IF(ISBLANK([Ezn_Efrag_Purchase_TOTAL]),0, IF([Ezn_Efrag_Purchase_TOTAL]<0, [Ezn_Efrag_Purchase_TOTAL]*(-1), [Ezn_Efrag_Purchase_TOTAL])), 
    
    "Period", 'B_Dim_Date_Decs'[taxperiod], 
    "Activity",   "غير معلوم",
    "ActivityL2", "غير معلوم",
     
    "SalesInOtherPurchasesTax", 0,
    "DeclarationID", 0,
    "Dim_Declarations[Dec_ID_S]", 0,  
    "SalesInOtherPurchases", 0,
    "PurchasesInOtherSales", 0,
    "SalesInvoicesCountInOthers", 0,
    "PurchaseInvoiceCountInOthers", 0,
    "TaxPayerID", 0

    
    )




'''
,

  '''
// DAX Query 56
DEFINE
  //VAR _tp="202003"
  
 // VAR __DS0FilterTable =  TREATAS({"إتفاقيات","جدول","قيمة مضافة"}, 'B_Dim_DeclarationTypes'[Name])

  VAR __DS0FilterTable2 = TREATAS({_tp}, 'B_Dim_Date_Decs'[Year_Quarter_Period])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionName],
          'A_Dim_Districts_Vat'[DistrictVat_Name],
          'B_Dim_Date_Decs'[Year_Quarter_Period],
          A_Dim_Region[RegionCode],
          A_Dim_Districts_Vat[DistrictVat_Code],
          
        //  __DS0FilterTable,
         // __DS0FilterTable2,
          
          "DEC_Sum_Sales_VAT", 'C_Dim_Declarations'[DEC_Sum_Sales_VAT],
          "Transaction_TOTAL_Net_Sales", 'D_Dim_Invoices_5asm_w_Ta7seel'[Transaction_TOTAL_Net_Sales],
          "Different_Sales_vat_5asm_w_ta7seel", 'C_Dim_Declarations'[Different_Sales_vat-5asm_w_ta7seel],
          "His_Reported_SALES_Product_Total_Net", 'D_Dim_Invoices_PORTAL'[His_Reported_SALES_Product_Total_Net],
          "DEC_Total_Table_Tax_Value", 'C_Dim_Declarations'[DEC_Total_Table_Tax_Value],
          "est5las_Sales_Flag", IGNORE('C_Dim_Declarations'[est5las_Sales_Flag])
        )
      ),
      AND(
        AND(
          AND(
            AND(
              AND([est5las_Sales_Flag] = 0, NOT(ISBLANK([DEC_Sum_Sales_VAT]))),
              [DEC_Sum_Sales_VAT] <> 0
            ),
            [Different_Sales_vat_5asm_w_ta7seel] < 0
          ),
          NOT(ISBLANK([Transaction_TOTAL_Net_Sales]))
        ),
        [Transaction_TOTAL_Net_Sales] <> 0
      )
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(

          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionName],
          'A_Dim_Districts_Vat'[DistrictVat_Name],
          'B_Dim_Date_Decs'[Year_Quarter_Period],
          A_Dim_Region[RegionCode],
          A_Dim_Districts_Vat[DistrictVat_Code],

    //  __DS0FilterTable,
     // __DS0FilterTable2,
      __ValueFilterDM1,
      
      "DEC_Sum_Sales_VAT",                    'C_Dim_Declarations'[DEC_Sum_Sales_VAT],
      "Transaction_TOTAL_Net_Sales",          'D_Dim_Invoices_5asm_w_Ta7seel'[Transaction_TOTAL_Net_Sales],
      "Different_Sales_vat_5asm_w_ta7seel",   'C_Dim_Declarations'[Different_Sales_vat-5asm_w_ta7seel],
      "His_Reported_SALES_Product_Total_Net", 'D_Dim_Invoices_PORTAL'[His_Reported_SALES_Product_Total_Net],
      "DEC_Total_Table_Tax_Value",            'C_Dim_Declarations'[DEC_Total_Table_Tax_Value]
    )

  

EVALUATE
SELECTCOLUMNS( __DS0Core,

    "UniqueTaxId",          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name",                 'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",              'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "Period",               'B_Dim_Date_Decs'[Year_Quarter_Period],   //'Dim_Date'[year_quarter_period]    
    "RegionId",             IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",             IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0, A_Dim_Districts_Vat[DistrictVat_Code]),
    "RegionName",           'A_Dim_Region'[RegionName],
    "DistrictVat_Name",     'A_Dim_Districts_Vat'[DistrictVat_Name],
    
    
    "DEC_Sum_Sales_VAT",                      IF(ISBLANK([DEC_Sum_Sales_VAT]), 0, 
                                              IF([DEC_Sum_Sales_VAT]<0, [DEC_Sum_Sales_VAT]*(-1), [DEC_Sum_Sales_VAT]) ),
    
    "Transaction_TOTAL_Net_Sales",            IF(ISBLANK([Transaction_TOTAL_Net_Sales]), 0, 
                                              IF([Transaction_TOTAL_Net_Sales]<0, [Transaction_TOTAL_Net_Sales]*(-1), [Transaction_TOTAL_Net_Sales]) ),
    
    "Different_Sales_vat_5asm_w_ta7seel",     IF(ISBLANK([Different_Sales_vat_5asm_w_ta7seel]), 0, 
                                              IF([Different_Sales_vat_5asm_w_ta7seel]<0, [Different_Sales_vat_5asm_w_ta7seel]*(-1), [Different_Sales_vat_5asm_w_ta7seel]) ),
    
    "His_Reported_SALES_Product_Total_Net",   IF(ISBLANK([His_Reported_SALES_Product_Total_Net]), 0, 
                                              IF([His_Reported_SALES_Product_Total_Net]<0, [His_Reported_SALES_Product_Total_Net]*(-1), [His_Reported_SALES_Product_Total_Net]) ),
    
    "DEC_Total_Table_Tax_Value",              IF(ISBLANK([DEC_Total_Table_Tax_Value]), 0, 
                                              IF([DEC_Total_Table_Tax_Value]<0, [DEC_Total_Table_Tax_Value]*(-1), [DEC_Total_Table_Tax_Value]) ),


    "TaxLoss",                                IF(ISBLANK([Different_Sales_vat_5asm_w_ta7seel]), 0, 
                                              IF([Different_Sales_vat_5asm_w_ta7seel]<0, [Different_Sales_vat_5asm_w_ta7seel]*(-1), [Different_Sales_vat_5asm_w_ta7seel]) ),
       
    "DeclarationID", 0,
    "TaxPayerID", 0,
    "PurchaseInvoiceCountInOthers", 0,
    "PurchasesInOtherSales", 0,
    "PurchaseInOtherSalesTax", 0,
    "SalesInOtherPurchases", 0,
    "SalesInvoicesCountInOthers", 0,
    "Activity",   "غير معلوم",
    "ActivityL2", "غير معلوم"

) 
 

''',

'''// DAX Query 57
DEFINE
//var _tp=@taxPeriodKey
   VAR __DS0FilterTable = 
    TREATAS({"جدول",
      "قيمة مضافة"}, 'B_Dim_DeclarationTypes'[Name])

 // VAR __DS0FilterTable2 =   TREATAS({_tp}, 'B_Dim_Date_Decs'[taxperiod])

  VAR __DS0FilterTable3 = 
    TREATAS({TRUE}, 'B_Dim_TaxPayers_Universe_B'[IS_Dummy])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
          'B_Dim_Date_Decs'[taxperiod],
          __DS0FilterTable,
         // __DS0FilterTable2,
          __DS0FilterTable3,
          "DEC_Sum_Sales_VAT", 'C_Dim_Declarations'[DEC_Sum_Sales_VAT],
          "DEC_Sum_Purchase_VAT", 'C_Dim_Declarations'[DEC_Sum_Purchase_VAT],
          "est5las_Purchase_Flag", IGNORE('C_Dim_Declarations'[est5las_Purchase_Flag]),
          "est5las_Sales_Flag", IGNORE('C_Dim_Declarations'[est5las_Sales_Flag])
        )
      ),
      AND(
        AND(
          AND([DEC_Sum_Purchase_VAT] > 0, NOT(ISBLANK([DEC_Sum_Purchase_VAT]))),
          [est5las_Purchase_Flag] = 0
        ),
        [est5las_Sales_Flag] = 0
      )
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(
   
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionCode],
          'A_Dim_Districts_Vat'[DistrictVat_Code],
          'B_Dim_Date_Decs'[taxperiod]
       ,
      __DS0FilterTable,
    //  __DS0FilterTable2,
      __DS0FilterTable3,
      __ValueFilterDM1,
      "DEC_Sum_Sales_VAT", 'C_Dim_Declarations'[DEC_Sum_Sales_VAT],
      "DEC_Sum_Purchase_VAT", 'C_Dim_Declarations'[DEC_Sum_Purchase_VAT]
    )
  
EVALUATE
SELECTCOLUMNS ( __DS0Core ,
 
    "UniqueTaxId",      'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name",             'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "Period",           'B_Dim_Date_Decs'[taxperiod],
    "RegionId",             IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",             IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0, A_Dim_Districts_Vat[DistrictVat_Code]),    
    "DEC_Sum_Sales_VAT",    IF(ISBLANK([DEC_Sum_Sales_VAT]),0, IF([DEC_Sum_Sales_VAT]<0, [DEC_Sum_Sales_VAT]*(-1), [DEC_Sum_Sales_VAT])) ,
    "DEC_Sum_Purchase_VAT", IF(ISBLANK([DEC_Sum_Purchase_VAT]),0, IF([DEC_Sum_Purchase_VAT]<0, [DEC_Sum_Purchase_VAT]*(-1), [DEC_Sum_Purchase_VAT])), 
    "TaxLoss",              IF(ISBLANK([DEC_Sum_Purchase_VAT]),0, IF([DEC_Sum_Purchase_VAT]<0, [DEC_Sum_Purchase_VAT]*(-1), [DEC_Sum_Purchase_VAT])), 

    
    //"TaxLoss",'Dim_Declarations'[Purchases_Vat_With_Dummy],
    
    "DeclarationID", 0,
    "TaxPayerID", 0,
    "PurchaseInvoiceCountInOthers", 0,
    "PurchasesInOtherSales", 0,
    "PurchaseInOtherSalesTax", 0,
    "SalesInOtherPurchasesTax", 0,
    "SalesInOtherPurchases", 0,
    "SalesInvoicesCountInOthers", 0,
    "Activity", "غير معلوم",
    "ActivityL2", "غير معلوم",
    "DeclaredSalesTax", 0

)


'''

,
'''// DAX Query 58
DEFINE
 // VAR _tp=@taxPeriodKey
  
  VAR __DS0FilterTable =  TREATAS( {"إتفاقيات" ,"جدول" ,"قيمة مضافة", BLANK(), "صفري"}, 'B_Dim_DeclarationTypes'[Name])

 // VAR __DS0FilterTable2 = TREATAS({_tp}, 'C_Dim_Declarations'[TaxPeriod])

  VAR __ValueFilterDM1 = 
    FILTER(
      KEEPFILTERS(
        SUMMARIZECOLUMNS(
          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionName],
          'A_Dim_Districts_Vat'[DistrictVat_Name],
          'B_Dim_Date_Decs'[taxperiod],
          A_Dim_Region[RegionCode],
          A_Dim_Districts_Vat[DistrictVat_Code],
          
          __DS0FilterTable,
         // __DS0FilterTable2, 
          
          "DEC_Total_Vat_Value",         'C_Dim_Declarations'[DEC_Total_Vat_Value],
          "DEC_Total_Table_Value",       'C_Dim_Declarations'[DEC_Total_Table_Value],
          "Portal_Total_Vat_Value",      'C_Dim_Payments'[Portal_Total_Vat_Value],
          "Portal_Total_Table_Value",    'C_Dim_Payments'[Portal_Total_Table_Value],
          "VAT_Debit",                   'C_Dim_Declarations'[VAT_Debit],
          "TABLE_Debit",                 'C_Dim_Declarations'[TABLE_Debit],
          "Total_TaxLoss_After_Payment", 'C_Dim_Declarations'[Total_TaxLoss_After_Payment],
          "est5las_Vat_Value_flag",      IGNORE('C_Dim_Declarations'[est5las_Vat_Value_flag])
        )
      ),
      AND([est5las_Vat_Value_flag] = 0, [Total_TaxLoss_After_Payment] > 0)
    )

  VAR __DS0Core = 
    SUMMARIZECOLUMNS(

          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
          'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
          'A_Dim_Region'[RegionName],
          'A_Dim_Districts_Vat'[DistrictVat_Name],
          'B_Dim_Date_Decs'[taxperiod],
          A_Dim_Region[RegionCode],
          A_Dim_Districts_Vat[DistrictVat_Code],          
          
      __DS0FilterTable,
    //  __DS0FilterTable2,
      __ValueFilterDM1,
      
      "DEC_Total_Vat_Value",          'C_Dim_Declarations'[DEC_Total_Vat_Value],
      "DEC_Total_Table_Value",        'C_Dim_Declarations'[DEC_Total_Table_Value],
      "Portal_Total_Vat_Value",       'C_Dim_Payments'[Portal_Total_Vat_Value],
      "Portal_Total_Table_Value",     'C_Dim_Payments'[Portal_Total_Table_Value],
      "VAT_Debit",                    'C_Dim_Declarations'[VAT_Debit],
      "TABLE_Debit",                  'C_Dim_Declarations'[TABLE_Debit],
      "Total_TaxLoss_After_Payment",  'C_Dim_Declarations'[Total_TaxLoss_After_Payment]
    )


EVALUATE
SELECTCOLUMNS( __DS0Core,

    "UniqueTaxId",          'B_Dim_Registered_TaxPayers_A'[Unique_Tax_Id],
    "Name",                 'B_Dim_Registered_TaxPayers_A'[Taxpayer_Name],
    "Address",              'B_Dim_Registered_TaxPayers_A'[Taxpayer_Address],
    "Period",               'B_Dim_Date_Decs'[taxperiod],   //'Dim_Date'[year_quarter_period]    
    "RegionId",             IF(ISBLANK(A_Dim_Region[RegionCode]), 0, A_Dim_Region[RegionCode]),
    "District",             IF(ISBLANK(A_Dim_Districts_Vat[DistrictVat_Code]), 0,    A_Dim_Districts_Vat[DistrictVat_Code]),
    "RegionName",           'A_Dim_Region'[RegionName],
    "DistrictVat_Name",     'A_Dim_Districts_Vat'[DistrictVat_Name],

    "DEC_Total_Vat_Value",      IF(ISBLANK([DEC_Total_Vat_Value]), 0, IF([DEC_Total_Vat_Value]<0, [DEC_Total_Vat_Value]*-1, [DEC_Total_Vat_Value])), 	
    
	"DEC_Total_Table_Value",    IF(ISBLANK([DEC_Total_Table_Value]), 0, IF([DEC_Total_Table_Value]<0, [DEC_Total_Table_Value]*-1, [DEC_Total_Table_Value])),	
    
	"Portal_Total_Vat_Value",   IF(ISBLANK([Portal_Total_Vat_Value]), 0, IF([Portal_Total_Vat_Value]<0, [Portal_Total_Vat_Value]*-1, [Portal_Total_Vat_Value])),	
    
	"Portal_Total_Table_Value", IF(ISBLANK([Portal_Total_Table_Value]), 0, IF([Portal_Total_Table_Value]<0, [Portal_Total_Table_Value]*-1, [Portal_Total_Table_Value])),
 
 
    "VAT_Debit",                IF(ISBLANK([VAT_Debit]), 0, IF([VAT_Debit]<0, [VAT_Debit]*-1, [VAT_Debit])),
    
    
    "TABLE_Debit",              IF(ISBLANK([TABLE_Debit]), 0, IF([TABLE_Debit]<0, [TABLE_Debit]*-1, [TABLE_Debit])),	
                   
	
     "TaxLoss",                IF(ISBLANK([Total_TaxLoss_After_Payment]),0, IF([Total_TaxLoss_After_Payment]<0, [Total_TaxLoss_After_Payment]*(-1), [Total_TaxLoss_After_Payment])),           
      // إجمالي المديونية بعد الدف
	  
	"DeclarationID", 0,
    "TaxPayerID", 0,
	"Activity",   "غير معلوم",
    "ActivityL2", "غير معلوم",
	"Dec_ID_S", 0,                
    "FK_TaxPayer_ID_S", 0, 
	"Declaration_ID", 0, 
	"TableTaxTotal", 0,  
	"Fk_Send_Date_ID", 0,  
    "Fk_Declaration_Type_ID_S", 0, 
    "Fk_VatType_ID_S", 0,     
    "Active", 0,   
    "Send_Time", 0,   
    "Fk_Link_Type_ID_S", 0
)	'''

]