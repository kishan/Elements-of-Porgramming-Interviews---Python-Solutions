# each client has a "credit" number which is a non-neg interger value
# ) Design a data structure that implements the following methods:
# 1. Insert: add a client with a credit, replacing any existing entry
# 2. Remove: delete the client
# 3. Lookup: return the number of credits for the client
# 4. Add-to-all: increment the credit count for all current clients by an amount
# 5. Max: Return client with maximum credits.


"""
Use a BST with the keys as credits and the values are the clients with that credit. 
Keep the current add-to-all value, initialized to 0, and as new elements are inserted, 
subtract the add-to-all value. When popping elements, add the add-to-all value to the 
node's credit. Additionally, maintain a hash map in which keys are clients and values 
are credits. Lookup simply involves searching the hash map and removal involves 
removing from the BST based on the credit value from the hash map.
"""



public class AddingCredits {
  // @include
  public static class ClientsCreditsInfo {
    private int offset = 0;
    private Map<String, Integer> clientToCredit = new HashMap<>();
    private NavigableMap<Integer, Set<String>> creditToClients
        = new TreeMap<>();

    public void insert(String clientID, int c) {
      remove(clientID);
      clientToCredit.put(clientID, c - offset);
      Set<String> set = creditToClients.get(c - offset);
      if (set == null) {
        set = new HashSet<>();
        creditToClients.put(c - offset, set);
      }
      set.add(clientID);
    }

    public boolean remove(String clientID) {
      Integer clientCredit = clientToCredit.get(clientID);
      if (clientCredit != null) {
        creditToClients.get(clientCredit).remove(clientID);
        if (creditToClients.get(clientCredit).isEmpty()) {
          creditToClients.remove(clientCredit);
        }
        clientToCredit.remove(clientID);
        return true;
      }
      return false;
    }

    public int lookup(String clientID) {
      Integer clientCredit = clientToCredit.get(clientID);
      return clientCredit == null ? -1 : clientCredit + offset;
    }

    public void addAll(int C) { offset += C; }

    public String max() {
      return creditToClients.isEmpty()
          ? ""
          : creditToClients.lastEntry().getValue().iterator().next();
    }
  }