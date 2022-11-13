import Search from "../../src/components/Search";

describe("Search", () => {
  it("Rendered", () => {
    cy.mount(<Search />);
    cy.get("input");
  });
});
