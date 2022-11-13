describe("Router", () => {
  beforeEach(() => {
    cy.visit("localhost:3000/");
  });
  it("Visit Home page", () => {
    cy.visit("localhost:3000/");
  });
  it("Visit Course page", () => {
    cy.visit("localhost:3000/course");
  });
  it("Visit Instructor page", () => {
    cy.visit("localhost:3000/instructor");
  });
});
