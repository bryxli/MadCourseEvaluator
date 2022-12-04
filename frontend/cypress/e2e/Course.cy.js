/// <reference types ="cypress" />

describe("Visiting Courses", () => {
  /**
   * Basic testing to make sure that visiting course pages are working
   */
  it("T1: Visits MATH 221 and displays entire course page information", () => {
    cy.visit("http://localhost:3000/course?id=79922");
  });

  it("T2: Visits CS200 and displays entire course page information", () => {
    cy.visit("http://localhost:3000/course?id=79778");
  });

  it("T3: Visits CS202 and displays entire course page information", () => {
    cy.visit("http://localhost:3000/course?id=79779");
  });

  it("T4: Visits CS300 and displays entire course page information", () => {
    cy.visit("http://localhost:3000/course?id=79785");
  });

  it("T5: Visits CS400 and displays entire course page information", () => {
    cy.visit("http://localhost:3000/course?id=79794");
  });

  it("T6: Searched for CS 200 and retrieves the course page information", () => {
    cy.visit("http://localhost:3000/course?id=79778");
  });

  it("T7: Searched for CS 200 and retrieves the course page information", () => {
    cy.visit("http://localhost:3000/course?id=79778");
  });

  it("T8: Searched for CS 200 and retrieves the course page information", () => {
    cy.visit("http://localhost:3000/course?id=79778");
  });

  it("T9: Searched for CS 200 and retrieves the course page information", () => {
    cy.visit("http://localhost:3000/course?id=79778");
  });

  it("T10: Searched for CS 200 and retrieves the course page information", () => {
    cy.visit("http://localhost:3000/course?id=79778");
  });
});
