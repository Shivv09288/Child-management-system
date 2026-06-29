package com.schoolmgmt.model;

import java.io.Serializable;

public class Parent implements Serializable {
    private static final long serialVersionUID = 1L;

    private int parentId;
    private int studentId;
    private String parentName;
    private String relationship;
    private String email;
    private String phone;
    private String occupation;
    private String address;
    private String city;
    private String state;
    private String postalCode;

    public Parent() {}

    public Parent(int studentId, String parentName, String relationship, String email,
                  String phone, String occupation, String address, String city, String state, String postalCode) {
        this.studentId = studentId;
        this.parentName = parentName;
        this.relationship = relationship;
        this.email = email;
        this.phone = phone;
        this.occupation = occupation;
        this.address = address;
        this.city = city;
        this.state = state;
        this.postalCode = postalCode;
    }

    public int getParentId() { return parentId; }
    public void setParentId(int parentId) { this.parentId = parentId; }

    public int getStudentId() { return studentId; }
    public void setStudentId(int studentId) { this.studentId = studentId; }

    public String getParentName() { return parentName; }
    public void setParentName(String parentName) { this.parentName = parentName; }

    public String getRelationship() { return relationship; }
    public void setRelationship(String relationship) { this.relationship = relationship; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }

    public String getOccupation() { return occupation; }
    public void setOccupation(String occupation) { this.occupation = occupation; }

    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }

    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }

    public String getState() { return state; }
    public void setState(String state) { this.state = state; }

    public String getPostalCode() { return postalCode; }
    public void setPostalCode(String postalCode) { this.postalCode = postalCode; }

    @Override
    public String toString() {
        return "Parent{" +
                "parentId=" + parentId +
                ", parentName='" + parentName + '\'' +
                ", relationship='" + relationship + '\'' +
                '}';
    }
}
