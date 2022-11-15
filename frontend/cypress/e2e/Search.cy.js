/* eslint-disable cypress/no-unnecessary-waiting */

describe("Search", () => {
  it("Search bar successfully retrieves all courses", () => {
    cy.visit("localhost:3000/");
    cy.get("input").then((search_bar) => {
      search_bar.click();
      // Wait for endpoint to load data
      cy.wait(1000);
      cy.get("div[id='search']").then((result) => {
        const search = result[1].children;
        // Replace 3 with number of courses to retrieve from endpoint
        expect(search).to.have.length(3);
      });
    });
  });
  it("Search bar successfully retrieves all professors", () => {
    throw new Error("todo");
  });
});
