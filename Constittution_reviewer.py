import PyPDF2
import sys

#open file as reading (r) in binary (b) mode
file = open("/Users/root1/Desktop/WarriorsforChristConstitution.pdf", 'rb')

officer_clause = "If an officer fails to maintain enrollment in the University, they shall resign and/or be removed from office immediately."
eligibility_clause = "Only current USF student members can hold office."
faculty_clause = "A full-time USF faculty or staff member will serve as an advisor."
member_clause = "All USF students who are members of the organization must be allowed to run for an E-Board/Officer position regardless of college/major."
amendment_clause = "Amendments must be submitted to, and are subject to review and approval by, the respective campus office responsible for student organizations for where the organization will primarily function."
anti_hazing_clause = '''This organization prohibits its members, both individually and collectively from committing any acts of hazing as defined herein: “Hazing" as defined by §1006.63, Florida Statutes, means any action or situation that recklessly or intentionally endangers the mental or physical health or safety of a student for purposes including, but not limited to, initiation or admission into or affiliation with any organization operating under the sanction of a postsecondary institution, regardless of a person’s willingness to participate. "Hazing" includes, but is not limited to, pressuring or coercing the student into violating state or federal law; any brutality of a physical nature, such as whipping, beating, branding, exposure to the elements, forced consumption of any food, liquor, drug, or other substance; or other forced physical activity that could adversely affect the physical health or safety of the student; and also includes any activity that would subject the student to extreme mental stress, such as sleep deprivation, forced exclusion from social contact, forced conduct that could result in extreme embarrassment, or other forced activity that could adversely affect the mental health or dignity of the student. Hazing does not include customary athletic events or other similar contests or competitions or any activity or conduct that furthers a legal and legitimate objective. In addition to Florida Statutes §1006.63, hazing as defined by the USF system also includes, but is not limited to, the forced use of alcohol; morally degrading or humiliating games and activities; physical and psychological shocks; deception; verbal abuse; personal servitude; kidnapping; deprivation of privileges granted to others in the organization by use of force or duress; and any other activities which are contrary to academic achievement, the stated purpose of the local and/or (inter)national organization, and/or the mission, policies or regulations of the USF system or applicable state law.'''
organization_agreement_clause = '''Organization agrees to comply with all university policies or procedures, as stated in the Student Handbook, Student Organization Handbook, and Code of Student Conduct, as well as any policies or procedures set forth by the respective campus’ office responsible for student organizations for where the organization will primarily function. If this organization applies for funding through the Student Government Activity and Service funding process, this organization agrees to abide by all Student Government policies.'''

reader = PyPDF2.PdfReader(file)
no_of_pages = len(reader.pages)

print(f"Total pages: {no_of_pages}.\n")
pdfcontent = ""
for i in range (no_of_pages):
    page = reader.pages[i]
    pdfcontent += (page.extract_text())

#print(pdfcontent)

if officer_clause in pdfcontent:
    print("Officer clause found.\n")
else:
    print("Officer clause not found.\n")

if eligibility_clause in pdfcontent:
    print("Eligibility clause found.\n")
else: 
    print("Eligibility clause not found.\n")

if faculty_clause in pdfcontent:
    print("Faculty clause found.\n")
else:
    print("Faculty clause not found.\n")

if member_clause in pdfcontent:
    print("Member clause found.\n")
else:
    print("Member clause not found.\n")

if amendment_clause in pdfcontent:
    print("Amendment clause found.\n")
else:
    print("Amendment clause not found.\n")

if anti_hazing_clause in pdfcontent:
    print("Anti-hazing clause found.\n")
else:
    print("Anti-hazing clause not found.\n")

if organization_agreement_clause in pdfcontent:
    print("Organization agreement clause found.\n")
else:
    print("Organization agreement clause not found.\n")