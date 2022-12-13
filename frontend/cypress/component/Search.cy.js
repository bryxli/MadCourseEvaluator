/**
 * Authors: Aidan Shine, Bryan Li, Jarvis Jia, Peter Bryant, Swathi Annamaneni, Tong Yang
 * Revision History: 11/01/2022:12/13/2022
 * Organization: Madgers
 * Version: 1.0.0
 */

import Search from "../../src/components/Search";

describe("Search", () => {
  // Test component rendered on page
  it("Rendered", () => {
    cy.mount(<Search />);
    cy.get("input");
  });
});
