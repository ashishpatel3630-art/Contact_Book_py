import streamlit as st
import requests



API="http://127.0.0.1:5000"



st.set_page_config(
    page_title="Contact Book",
    page_icon="📒"
)


st.title("📒 Advanced Contact Book")



menu = st.sidebar.selectbox(
    "Menu",
    [
        "View Contacts",
        "Add Contact",
        "Update Contact",
        "Delete Contact",
        "Search"
    ]
)



# VIEW

if menu=="View Contacts":


    try:

        data=requests.get(
            f"{API}/contacts"
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


    except:

        st.error(
            "Backend not running"
        )




# ADD

elif menu=="Add Contact":


    name=st.text_input("Name")

    phone=st.text_input("Phone")

    email=st.text_input("Email")


    if st.button("Save"):


        response=requests.post(
            f"{API}/add",
            json={
                "name":name,
                "phone":phone,
                "email":email
            }
        )


        st.success(
            response.json()["message"]
        )




# UPDATE


elif menu=="Update Contact":


    name=st.text_input("Name")

    phone=st.text_input("New Phone")

    email=st.text_input("New Email")


    if st.button("Update"):


        response=requests.put(
            f"{API}/update/{name}",
            json={
                "phone":phone,
                "email":email
            }
        )


        st.success(
            response.json()["message"]
        )





# DELETE


elif menu=="Delete Contact":


    name=st.text_input(
        "Contact Name"
    )


    if st.button("Delete"):


        response=requests.delete(
            f"{API}/delete/{name}"
        )


        st.success(
            response.json()["message"]
        )





# SEARCH


elif menu=="Search":


    name=st.text_input(
        "Search Name"
    )


    if st.button("Find"):


        data=requests.get(
            f"{API}/search/{name}"
        ).json()


        st.json(data)