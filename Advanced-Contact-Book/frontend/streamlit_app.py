import streamlit as st
import requests


API="http://127.0.0.1:5000"



st.title("📒 Contact Book Manager")


menu=st.sidebar.selectbox(
    "Menu",
    [
        "View Contacts",
        "Add Contact",
        "Delete Contact"
    ]
)



if menu=="View Contacts":

    data=requests.get(
        API+"/contacts"
    ).json()


    for name,info in data.items():

        st.subheader(name)

        st.write(
            "📞",
            info["phone"]
        )

        st.write(
            "📧",
            info["email"]
        )

        st.divider()



elif menu=="Add Contact":


    name=st.text_input("Name")

    phone=st.text_input("Phone")

    email=st.text_input("Email")



    if st.button("Save"):


        requests.post(
            API+"/add",
            json={
                "name":name,
                "phone":phone,
                "email":email
            }
        )


        st.success(
            "Contact Added"
        )



elif menu=="Delete Contact":


    name=st.text_input(
        "Contact Name"
    )


    if st.button("Delete"):

        requests.delete(
            API+f"/delete/{name}"
        )


        st.success(
            "Deleted"
        )