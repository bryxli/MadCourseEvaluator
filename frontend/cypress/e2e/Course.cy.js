/// <reference types ="cypress" />

describe("Test Visiting Courses", () => {
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
});

describe("Test Contents of Course Page", () => {
  it("T1: Contains Web Page Title", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.contains("Madger Courses");
  });

  it("T2: Contains Subject", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.contains("Subject");
  });

  it("T3: Contains Credits", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.contains("Credits");
  });

  it("T4: Contains Description", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.contains("Description");
  });

  it("T5: Contains Instructors", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.contains("Instructors");
  });

  it("T6: Contains Instructors", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.contains("Instructors");
  });

  it("T7: Contains Course Title", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.get("[class$=bold-heading-style]");
    cy.get("[class$=heading-style]");
  });

  it("T8: Contains Reddit Icon", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.get("[alt$=reddit-logo]");
  });

  it("T9: Contains Graph", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.get("[class$=recharts-wrapper]");
  });

  it("T10: Contains Reddit Box", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.get("[class$=reddit-box-body]");
  });

  it("T11: Contains Search bar", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.get("[class$=rbt]");
  });

  it("T12: Contains Professor List", () => {
    cy.visit("http://localhost:3000/course?id=79922");
    cy.get("[class$=professor-list]");
  });
});

describe("Test Reddit List Content in Course Page", () => {
  // it("T11: Click content in reddit comments", () => {
  //   cy.visit("http://localhost:3000/course?id=79922");
  //   cy.wait(10000);
  //   cy.get('[class$=reddit-list-item]');
});

describe("Test Professor List Content in Course Page", () => {
  // it("T11: Click content in reddit comments", () => {
  //   cy.visit("http://localhost:3000/course?id=79922");
  //   cy.wait(10000);
  //   cy.get('[class$=reddit-list-item]');
  // });
});
