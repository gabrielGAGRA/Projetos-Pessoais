using backend.Domain.Entities;

namespace backend.Application.Interfaces
{
    public interface IAccountService
    {
        Task<Account> GetAccountAsync(int accountId);
        Task<decimal> GetBalanceAsync(int accountId);
        Task<List<Transaction>> GetTransactionHistoryAsync(int accountId);
        Task<bool> BuyCurrencyAsync(int accountId, string currencyFrom, string currencyTo, decimal amount);
    }
}