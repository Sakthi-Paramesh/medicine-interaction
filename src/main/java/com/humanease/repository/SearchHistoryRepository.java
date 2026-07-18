package com.humanease.repository;

import com.humanease.entity.SearchHistory;
import com.humanease.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface SearchHistoryRepository extends JpaRepository<SearchHistory, Long> {
    List<SearchHistory> findTop10ByUserOrderBySearchedAtDesc(User user);
}
